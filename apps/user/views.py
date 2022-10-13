from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action

from apps.user.models import User
from apps.user.permissions import IsAdmin, IsCliente

from apps.user.serializers import UserSerializer, SetPasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # queryset = User.objects.all()
    ordering_fields = ['id', 'username', 'email']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete',
                           'set_password']:
            permission_classes = (IsAuthenticated, IsAdmin)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated, IsAdmin | IsCliente )
        else:
            permission_classes = (IsAuthenticated, )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        if user.type in [User.Type.EDITORIAL, User.Type.AUTOR]:
            queryset = queryset.filter(id=user.id)

        return queryset

    @action(detail=True, methods=['post'], url_path=r'set-password')
    def set_password(self, request, *args, **kwargs):
        serializer = SetPasswordSerializer(instance=self.get_object(),
                                           data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Login(ObtainAuthToken): #genera un token para manejar la seguridad
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={
            'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user_id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'type': user.type
            }
        )


class Logout(APIView): #elimina el token al cerrar cesion
    def post(self, request, *args, **kwargs):
        user = request.user
        Token.objects.filter(user=user).delete()

        return Response({'message': 'Exito'})

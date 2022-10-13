from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    # type = serializers.IntegerField()

    class Meta:
        model = User
        # fields = '__all__' //para todos los campos
        # fields = ['id', 'first_name']
        exclude = ['groups', 'password', 'user_permissions', 'is_active',
                   'is_superuser', 'is_staff']
        # exclude = []//para todos los campos (no se excluye nada)


class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']

        if password != confirm_password:
            raise ValidationError('Las contraseñas no coinciden.')

        return attrs

from django.contrib import admin
from django.urls import path, re_path, include

from apps.user.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    re_path(r'^', include('apps.user.urls')),

]

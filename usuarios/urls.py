"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Importa tu archivo views.py

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/inicio_sesion.html'), name='login'),
    
    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Recuperación de contraseña 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuarios/recuperar_contraseña.html"), name='password_reset'),
    
    # Registro 
    path('registro/', views.registro_view, name='registro'),
]
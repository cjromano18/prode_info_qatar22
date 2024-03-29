from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='home'),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name="login.html"), name= 'login'),
    path('cerrar-sesion/', auth_views.logout_then_login, name="logout"),
    path('mis-grupos/', views.MisGrupos.as_view(), name= 'mis_grupos')
]

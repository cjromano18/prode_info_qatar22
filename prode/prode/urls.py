from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='home'),
    path('iniciar-sesión/', views.login, name= 'login'),
    path('mis-grupos/', views.MisGrupos.as_view(), name= 'mis_grupos')
]

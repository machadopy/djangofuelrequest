from django.urls import path

from .views import index, contato, ver_plano

urlpatterns = [
    path('', index),
    path('contato/', contato, name='contato'),
    path('ver_plano/<int:pk>', ver_plano , name = 'ver_plano' ),
]
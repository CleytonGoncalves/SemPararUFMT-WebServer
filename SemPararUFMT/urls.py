from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Checar passagem
    path('check/<tag_uid>/', views.check_passagem, name='check-passagem')
]

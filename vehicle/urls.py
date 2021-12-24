from django.urls import path
from . import views


urlpatterns = [
    path('cars', views.cars, name='cars'),
    path('popular', views.popular, name='popular'),
    path('delete/<int:car_id>/', views.delete, name='delete'),
    path('rate', views.rate, name='rate'),
]
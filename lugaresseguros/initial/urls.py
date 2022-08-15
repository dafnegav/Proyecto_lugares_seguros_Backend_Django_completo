from django.urls import path
from initial import views

urlpatterns = [
    path('Saludos', views.HelloDrf.as_view(), name='index'),
] #as_view le dice a django que va a uncionar como una vista
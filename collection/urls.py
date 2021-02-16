from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='collection-home'),
    path('about/', views.about, name='collection-about'),
]
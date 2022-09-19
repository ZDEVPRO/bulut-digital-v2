from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

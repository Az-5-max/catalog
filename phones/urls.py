from django.urls import path
from phones import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.phone_detail, name='phone_detail'),
]
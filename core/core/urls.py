from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('auth/', views.auth_view, name='auth_view'),
    path('verify/', views.verify_view, name='verify_view'),
    path('verifyed/', views.verified_view, name='verified_view')
]

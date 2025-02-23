from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('live_condition/', views.live_condition, name='live_condition'),
    path('medical_record/', views.medical_record, name='medical_record'),
    path('patients/', views.patients, name='patients'),
    path('patient_status/', views.patient_status, name='patient_status'),
]
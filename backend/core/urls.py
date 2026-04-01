from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('clinicappointments/', views.clinicappointment_list, name='clinicappointment_list'),
    path('clinicappointments/create/', views.clinicappointment_create, name='clinicappointment_create'),
    path('clinicappointments/<int:pk>/edit/', views.clinicappointment_edit, name='clinicappointment_edit'),
    path('clinicappointments/<int:pk>/delete/', views.clinicappointment_delete, name='clinicappointment_delete'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/create/', views.prescription_create, name='prescription_create'),
    path('prescriptions/<int:pk>/edit/', views.prescription_edit, name='prescription_edit'),
    path('prescriptions/<int:pk>/delete/', views.prescription_delete, name='prescription_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]

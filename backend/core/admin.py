from django.contrib import admin
from .models import Patient, ClinicAppointment, Prescription

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "gender", "phone", "email", "created_at"]
    list_filter = ["gender", "status"]
    search_fields = ["name", "phone", "email"]

@admin.register(ClinicAppointment)
class ClinicAppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "doctor", "date", "time_slot", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["patient_name", "doctor", "time_slot"]

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "doctor", "date", "follow_up_date", "created_at"]
    search_fields = ["patient_name", "doctor"]

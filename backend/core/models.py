from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, choices=[("male", "Male"), ("female", "Female"), ("other", "Other")], default="male")
    phone = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    blood_group = models.CharField(max_length=255, blank=True, default="")
    allergies = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    last_visit = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ClinicAppointment(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    time_slot = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("checked_in", "Checked In"), ("completed", "Completed"), ("cancelled", "Cancelled"), ("no_show", "No Show")], default="scheduled")
    reason = models.TextField(blank=True, default="")
    prescription = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.patient_name

class Prescription(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255, blank=True, default="")
    diagnosis = models.TextField(blank=True, default="")
    medications = models.TextField(blank=True, default="")
    date = models.DateField(null=True, blank=True)
    follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.patient_name

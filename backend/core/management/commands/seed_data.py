from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Patient, ClinicAppointment, Prescription
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusClinic with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusclinic.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Patient.objects.count() == 0:
            for i in range(10):
                Patient.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    age=random.randint(1, 100),
                    gender=random.choice(["male", "female", "other"]),
                    phone=f"+91-98765{43210+i}",
                    email=f"demo{i+1}@example.com",
                    blood_group=f"Sample {i+1}",
                    allergies=f"Sample allergies for record {i+1}",
                    status=random.choice(["active", "inactive"]),
                    last_visit=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Patient records created'))

        if ClinicAppointment.objects.count() == 0:
            for i in range(10):
                ClinicAppointment.objects.create(
                    patient_name=f"Sample ClinicAppointment {i+1}",
                    doctor=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    time_slot=f"Sample {i+1}",
                    status=random.choice(["scheduled", "checked_in", "completed", "cancelled", "no_show"]),
                    reason=f"Sample reason for record {i+1}",
                    prescription=f"Sample prescription for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ClinicAppointment records created'))

        if Prescription.objects.count() == 0:
            for i in range(10):
                Prescription.objects.create(
                    patient_name=f"Sample Prescription {i+1}",
                    doctor=f"Sample {i+1}",
                    diagnosis=f"Sample diagnosis for record {i+1}",
                    medications=f"Sample medications for record {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    follow_up_date=date.today() - timedelta(days=random.randint(0, 90)),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Prescription records created'))

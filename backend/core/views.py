import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Patient, ClinicAppointment, Prescription


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['patient_count'] = Patient.objects.count()
    ctx['patient_male'] = Patient.objects.filter(gender='male').count()
    ctx['patient_female'] = Patient.objects.filter(gender='female').count()
    ctx['patient_other'] = Patient.objects.filter(gender='other').count()
    ctx['clinicappointment_count'] = ClinicAppointment.objects.count()
    ctx['clinicappointment_scheduled'] = ClinicAppointment.objects.filter(status='scheduled').count()
    ctx['clinicappointment_checked_in'] = ClinicAppointment.objects.filter(status='checked_in').count()
    ctx['clinicappointment_completed'] = ClinicAppointment.objects.filter(status='completed').count()
    ctx['prescription_count'] = Prescription.objects.count()
    ctx['recent'] = Patient.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def patient_list(request):
    qs = Patient.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(gender=status_filter)
    return render(request, 'patient_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def patient_create(request):
    if request.method == 'POST':
        obj = Patient()
        obj.name = request.POST.get('name', '')
        obj.age = request.POST.get('age') or 0
        obj.gender = request.POST.get('gender', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.blood_group = request.POST.get('blood_group', '')
        obj.allergies = request.POST.get('allergies', '')
        obj.status = request.POST.get('status', '')
        obj.last_visit = request.POST.get('last_visit') or None
        obj.save()
        return redirect('/patients/')
    return render(request, 'patient_form.html', {'editing': False})


@login_required
def patient_edit(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.age = request.POST.get('age') or 0
        obj.gender = request.POST.get('gender', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.blood_group = request.POST.get('blood_group', '')
        obj.allergies = request.POST.get('allergies', '')
        obj.status = request.POST.get('status', '')
        obj.last_visit = request.POST.get('last_visit') or None
        obj.save()
        return redirect('/patients/')
    return render(request, 'patient_form.html', {'record': obj, 'editing': True})


@login_required
def patient_delete(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/patients/')


@login_required
def clinicappointment_list(request):
    qs = ClinicAppointment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(patient_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'clinicappointment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def clinicappointment_create(request):
    if request.method == 'POST':
        obj = ClinicAppointment()
        obj.patient_name = request.POST.get('patient_name', '')
        obj.doctor = request.POST.get('doctor', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.reason = request.POST.get('reason', '')
        obj.prescription = request.POST.get('prescription', '')
        obj.save()
        return redirect('/clinicappointments/')
    return render(request, 'clinicappointment_form.html', {'editing': False})


@login_required
def clinicappointment_edit(request, pk):
    obj = get_object_or_404(ClinicAppointment, pk=pk)
    if request.method == 'POST':
        obj.patient_name = request.POST.get('patient_name', '')
        obj.doctor = request.POST.get('doctor', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.reason = request.POST.get('reason', '')
        obj.prescription = request.POST.get('prescription', '')
        obj.save()
        return redirect('/clinicappointments/')
    return render(request, 'clinicappointment_form.html', {'record': obj, 'editing': True})


@login_required
def clinicappointment_delete(request, pk):
    obj = get_object_or_404(ClinicAppointment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/clinicappointments/')


@login_required
def prescription_list(request):
    qs = Prescription.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(patient_name__icontains=search)
    status_filter = ''
    return render(request, 'prescription_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def prescription_create(request):
    if request.method == 'POST':
        obj = Prescription()
        obj.patient_name = request.POST.get('patient_name', '')
        obj.doctor = request.POST.get('doctor', '')
        obj.diagnosis = request.POST.get('diagnosis', '')
        obj.medications = request.POST.get('medications', '')
        obj.date = request.POST.get('date') or None
        obj.follow_up_date = request.POST.get('follow_up_date') or None
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/prescriptions/')
    return render(request, 'prescription_form.html', {'editing': False})


@login_required
def prescription_edit(request, pk):
    obj = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        obj.patient_name = request.POST.get('patient_name', '')
        obj.doctor = request.POST.get('doctor', '')
        obj.diagnosis = request.POST.get('diagnosis', '')
        obj.medications = request.POST.get('medications', '')
        obj.date = request.POST.get('date') or None
        obj.follow_up_date = request.POST.get('follow_up_date') or None
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/prescriptions/')
    return render(request, 'prescription_form.html', {'record': obj, 'editing': True})


@login_required
def prescription_delete(request, pk):
    obj = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/prescriptions/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['patient_count'] = Patient.objects.count()
    data['clinicappointment_count'] = ClinicAppointment.objects.count()
    data['prescription_count'] = Prescription.objects.count()
    return JsonResponse(data)

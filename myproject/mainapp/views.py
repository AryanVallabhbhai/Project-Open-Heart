from django.shortcuts import render

def home(request):
    return render(request, 'index.html',)

def login(request):
    if request.method == 'POST'
    return render(request, 'login.html')

def live_condition(request):
    return render(request, 'live_condition.html')

def medical_record(request):
    return render(request, 'medical_record.html')

def patients(request):
    return render(request, 'patients.html')

def patient_status(request):
    return render(request, 'patient_status.html')


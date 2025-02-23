from django.db import models

# Patient main table: holds only the unique patient ID.
class Patient(models.Model):
    def __str__(self):
        return f"Patient {self.id}"


# History table for patient information snapshots.
class PatientHistory(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='histories')
    first_name = models.CharField(max_length=100)   # Max length: 100
    last_name = models.CharField(max_length=100)    # Max length: 100
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Other')  # Max length: 6
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)  # Max length: 3
    age = models.PositiveIntegerField()  # Must be positive (years)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # 5 digits total, 2 decimal points
    allergy = models.TextField(default='None')  # No binding length for allergy
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        return self.timestamp.strftime("%m/%d/%y %H:%M")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} at {self.formatted_timestamp()}"


# Faculty model remains unchanged.
class Faculty(models.Model):
    CLEARANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    clearance = models.CharField(max_length=6, choices=CLEARANCE_CHOICES)
    
    def __str__(self):
        return self.name


# Live Condition Data for a patient.
class LiveConditionData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    respiration_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)
    o2_saturation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_sugar = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pain_level = models.PositiveIntegerField(null=True, blank=True)
    sleep_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        return self.timestamp.strftime("%m/%d/%y %H:%M")
    
    def __str__(self):
        return f"Live condition data for Patient {self.patient.id} at {self.formatted_timestamp()}"


# Audit log for Live Condition Data changes.
class LiveConditionDataAudit(models.Model):
    ACTION_CHOICES = [
        ('INSERT', 'INSERT'),
        ('UPDATE', 'UPDATE'),
        ('DELETE', 'DELETE'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data = models.ForeignKey(LiveConditionData, on_delete=models.CASCADE)
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    old_values = models.TextField(null=True, blank=True)
    new_values = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        return self.timestamp.strftime("%m/%d/%y %H:%M")
    
    def __str__(self):
        return f"{self.action} action for Patient {self.patient.id} at {self.formatted_timestamp()}"

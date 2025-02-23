from django.contrib import admin
from mainapp.models import Patient
from mainapp.models import Faculty
from mainapp.models import LiveConditionData
from mainapp.models import LiveConditionDataAudit


# Register your models here.

admin.site.register(Patient)
admin.site.register(Faculty)
admin.site.register(LiveConditionData)
admin.site.register(LiveConditionDataAudit)

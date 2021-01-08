from django.contrib import admin
from .models import Doctor,Patient,Appointment

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('id','name')

class PatientAdmin(admin.ModelAdmin):
	list_display = ('id','name')

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('id','doctor_id','patient_id','start_time','end_time')

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment,AppointmentAdmin)
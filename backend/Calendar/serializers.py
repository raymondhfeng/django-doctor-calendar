from rest_framework import serializers
from .models import Doctor,Patient,Appointment

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = ('id','name')

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ('id','name')

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ('id','doctor_id','patient_id','start_time','end_time')
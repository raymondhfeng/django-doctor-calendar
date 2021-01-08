from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorSerializer,PatientSerializer,AppointmentSerializer
from .models import Doctor,Patient,Appointment
from django.http import HttpResponseBadRequest

from datetime import datetime
import collections 

bookings = collections.defaultdict(list)
double_bookings = collections.defaultdict(list)
triple_bookings = collections.defaultdict(list)

class DoctorView(viewsets.ModelViewSet):
	serializer_class = DoctorSerializer
	queryset = Doctor.objects.all()

class PatientView(viewsets.ModelViewSet):
	serializer_class = PatientSerializer
	queryset = Patient.objects.all()

class AppointmentView(viewsets.ModelViewSet):
	serializer_class = AppointmentSerializer
	
	def get_queryset(self):
		queryset = Appointment.objects.all()
		if 'date' in self.request.query_params:
			date = self.request.query_params['date']
			queryset=queryset.filter(start_time__date=date)
		if 'doctor_id' in self.request.query_params:
			doctor_id = self.request.query_params['doctor_id']
			queryset = queryset.filter(doctor_id=doctor_id)
		return queryset

	def create(self,request):
		global bookings,double_bookings,triple_bookings
		start = datetime.strptime(request.data['start_time'],"%Y-%m-%dT%H:%M")
		end = datetime.strptime(request.data['end_time'],"%Y-%m-%dT%H:%M")
		baseline = datetime(2020,12,31)
		if start > end:
			return HttpResponseBadRequest("Invalid appointment")
		start_delta = start-baseline
		end_delta = end-baseline
		if (start_delta.seconds // 60) % 15 != 0 or (end_delta.seconds // 60) % 15 != 0:
			return HttpResponseBadRequest("Invalid appointment")

		doctor_id = request.data["doctor_id"]
		for i,j in triple_bookings[doctor_id]:
			if start < j and end > i:
				return HttpResponseBadRequest("Invalid appointment")
		for i,j in double_bookings[doctor_id]:
			if start < j and end > i:
				triple_bookings[doctor_id].append((max(start,i),min(end,j)))
				break
		else:
			for i,j in bookings[doctor_id]:
				if start < j and end > i:
					double_bookings[doctor_id].append((max(start,i),min(end,j)))
					break
			else:
				bookings[doctor_id].append((start,end))

		return super().create(request)

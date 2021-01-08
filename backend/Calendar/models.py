from django.db import models
import uuid

class Doctor(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	name = models.CharField(max_length=120)

	def _str_(self):
		return self.name

class Patient(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	name = models.CharField(max_length=120)

	def _str_(self):
		return self.name

class Appointment(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
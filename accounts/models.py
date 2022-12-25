from django.db import models
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os

# Create your models here.

class Students(models.Model):
	id = models.BigAutoField(primary_key=True)
	
	STATUS = (
			('Authorized', 'Authorized'),
			('Unauthorized', 'Unauthorized'),
			)
	employee_code = models.CharField(max_length=200, null=False, blank=False, unique=True)
	gender = models.CharField(max_length=50, choices=(("Male","Male"), ("Female","Female")),null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	dob = models.DateField( null=True, blank=True)
	blood_g = models.CharField(max_length=200, null=True,blank=True) 
	phone = models.CharField(max_length=200, null=True,blank=True)
	email = models.CharField(max_length=200, null=True,blank=True)
	department = models.TextField(max_length=200,null=True, blank=True)
	position = models.TextField(max_length=200, null=True, blank=True)
	date_added = models.DateField( null=True, blank=True)
	date_end = models.DateField(null=True, blank=True)
	employment_status = models.CharField(max_length=200, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)

	Image = models.ImageField(null=True, blank= False)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Students, self).save(*args, **kwargs)
		print(self.Image)
		imag = Image.open(self.Image.path)
		if imag.width > 200 or imag.height> 200:
			output_size = (156, 184)
			imag.thumbnail(output_size)
			imag.save(self.Image.path)



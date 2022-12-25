from tkinter import Widget
from django.forms import ModelForm , widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminEmailInputWidget
from .models import *
from django import forms

class EmployeeForm(ModelForm):
	class Meta:
		model = Students
		fields = '__all__'

		widgets = {
			'employee_code' : forms.TextInput(attrs={'class':'form-control'}),
			'blood_g' : forms.TextInput(attrs={'class':'form-control'}),
			'gender' : forms.Select(attrs={'class':'form-control'}),
			"dob" : forms.SelectDateWidget(years=range(1950, 2050),),
			'name' : forms.TextInput(attrs={'class':'form-control'}),
			'phone' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.TextInput(attrs={'class':'form-control'}),
			'department' : forms.TextInput(attrs={'class':'form-control'}),
			'position' : forms.TextInput(attrs={'class':'form-control'}),
			"date_added" : forms.SelectDateWidget(years=range(1950, 2050),),
			"date_end" : forms.SelectDateWidget(years=range(1950, 2050),),

		}






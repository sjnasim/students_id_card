from telnetlib import STATUS
from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

from django.utils.http import urlencode

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login1.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):

	
	employee = Students.objects.all()
	total_emp = employee.count()
	auth_emp = employee.filter(status='Authorized').count()
	unauth_emp = employee.filter(status='Unauthorized').count()
	context = {'employee':employee, 'total_emp':total_emp,
	'auth_emp':auth_emp,
	'unauth_emp':unauth_emp}

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def createEmp(request):
	
	form = EmployeeForm()

	if request.method == 'POST':
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
		else: 
			messages.success(request,"Employee ID already exist!")


	context = {'form':form}
	return render(request, 'accounts/create_emp.html', context)

@login_required(login_url='login')
def updateEmp(request, pk):
	emp = Students.objects.get(employee_code=pk)
	form = EmployeeForm(instance=emp)
	
	if request.method == 'POST':

		form = EmployeeForm(request.POST,request.FILES, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/')
		else: 
			messages.success(request,"Employee ID already exist!")
		

	context = {'form':form}
	return render(request, 'accounts/updateEmp.html', context)
	

def idCard(request,pk):
	#authentication.html?emp_id=
	# test = "authentication.html?emp_id="

	e = Students.objects.get(employee_code = pk)
	
	# url = e + '?' + urlencode({redirect_field_name: next_url})

	
	
	context = {"e":e}
	return render(request, 'accounts/id_card1.html', context)
	
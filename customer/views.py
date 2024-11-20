from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Customer
from . forms import RecordsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
import csv
from django.http import HttpResponse


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Generates a pdf presentation of the record
def pdf_record(request):
	# Create Bytestream buffer
	buf = io.BytesIO()

	# Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

	# Create a text object to tell us what to put on the canvas
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	
	# Designate model
	records = Customer.objects.all()

	# Create blank list
	lines = []

	for record in records:
		lines.append(record.first_name)
		lines.append(record.last_name)
		lines.append(record.email)
		lines.append(record.city)
		lines.append(record.phone)
		lines.append(record.date)
		lines.append("-----------------------------------")


	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Resturn result
	return FileResponse(buf, as_attachment=True, filename='record.pdf')



# View function for creating a CSV (Excel sheet) for all the records
def csv_record(request):
	response = HttpResponse(content_type='text/css')
	response['Content-Disposition'] = 'attachment; filename=record.csv'

	# Create writer
	writer = csv.writer(response)

	# Designate model
	records = Customer.objects.all()

	# Add column headings
	writer.writerow(['First Name','Last Name','Email address','County','Contact','Date'])

	# Loop through model and out put values
	for record in records:
		writer.writerow([record.first_name, record.last_name, record.email, record.city, record.phone, record.date])

	return response

def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Registered!!!!!!!!!!!'))
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register_user.html', {'form':form})



# View function for searching a record from the database
def search_record(request):
	if request.method == "POST":
		searched = request.POST['searched']
		records = Customer.objects.filter(first_name__contains=searched)
	return render(request, 'search_record.html', {'searched':searched,'records':records})



# View function that shows an individual record
def show_record(request, record_id):
	record = Customer.objects.get(pk=record_id)
	return render(request, 'show_record.html', {'record':record})


# View function that deletes a record
def delete_record(request, record_id):
	record = Customer.objects.get(pk=record_id)
	record.delete()
	messages.success(request, ('Record Deleted successfully'))
	return redirect('home')


# View function that updates a record
def update_record(request, record_id):
	record = Customer.objects.get(pk=record_id)
	form = RecordsForm(request.POST or None, instance=record)
	if form.is_valid():
		form.save()
		messages.success(request, ('Record Updated successfully'))
		return redirect('home')
	return render(request, 'update_record.html', {'record':record,'form':form})



# View function for the home page
def index(request):
	records = Customer.objects.all()
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You are successfully Loged In!'))
			return redirect('home')
		else:
			messages.success(request, ('Incorrect username or password, please try again'))
			return redirect('home')
	customer_count = Customer.objects.all().count()
	return render(request, 'index.html', {'customer_count':customer_count,'records':records})



# View function the logsout the user
def logout_user(request):
	logout(request)
	return redirect('home')



# View function that addas a new record
def add_record(request):
	submitted = False
	if request.method == "POST":
		form = RecordsForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('Customer Record added successfully'))
			return HttpResponseRedirect('/?submitted=True')
	else:
		form = RecordsForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'add_record.html', {'form':form})



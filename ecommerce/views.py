from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission  # Import the model

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'contact.html')  # Redirect to avoid resubmission
            print("Form submitted successfully")  # Add this line
        else:
            messages.error(request, "Please fill in all fields.")
        
    return render(request, 'contact.html')
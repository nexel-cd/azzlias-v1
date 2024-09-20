from django.contrib import admin
from .models import ContactSubmission

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Display these fields in the admin

admin.site.register(ContactSubmission, ContactSubmissionAdmin)

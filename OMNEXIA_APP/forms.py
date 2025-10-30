from django import forms
from .models import Contact, JobApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}),
            'company': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Company (optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your Message', 'rows': 5}),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applicant_name', 'applicant_email', 'applicant_phone', 'cover_letter', 'resume']
        widgets = {
            'applicant_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full Name'}),
            'applicant_email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'applicant_phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Why are you interested in this position?', 'rows': 4}),
            'resume': forms.FileInput(attrs={'class': 'form-file'}),
        }
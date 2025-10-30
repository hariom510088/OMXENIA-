from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Product, TeamMember, Project, JobOpening, Contact, JobApplication
from .forms import ContactForm, JobApplicationForm

def index(request):
    services = Service.objects.filter(featured=True)[:3]
    products = Product.objects.all()[:4]
    team_members = TeamMember.objects.all()[:3]
    projects = Project.objects.all()[:3]
    
    context = {
        'services': services,
        'products': products,
        'team_members': team_members,
        'projects': projects,
    }
    return render(request, 'OMNEXIA_APP/index.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'OMNEXIA_APP/about.html', {'team_members': team_members})

def services(request):
    services = Service.objects.all()
    return render(request, 'OMNEXIA_APP/services.html', {'services': services})

def solutions(request):
    services = Service.objects.all()
    return render(request, 'OMNEXIA_APP/solutions.html', {'services': services})

def products(request):
    products = Product.objects.all()
    return render(request, 'OMNEXIA_APP/products.html', {'products': products})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'OMNEXIA_APP/projects.html', {'projects': projects})

def careers(request):
    job_openings = JobOpening.objects.filter(is_active=True)
    return render(request, 'OMNEXIA_APP/careers.html', {'job_openings': job_openings})

def job_detail(request, job_id):
    job = JobOpening.objects.get(id=job_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            
            # Send email notification
            subject = f'New Job Application: {job.title}'
            message = f'''
            New job application received:
            
            Position: {job.title}
            Applicant: {application.applicant_name}
            Email: {application.applicant_email}
            Phone: {application.applicant_phone}
            
            Cover Letter:
            {application.cover_letter}
            '''
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['sabkabaap060@gmail.com'],  # HR email
                fail_silently=False,
            )
            
            return redirect('careers')
    else:
        form = JobApplicationForm()
    
    return render(request, 'OMNEXIA_APP/job_detail.html', {'job': job, 'form': form})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification
            subject = f'New Contact Form: {contact.subject}'
            message = f'''
            New contact form submission:
            
            Name: {contact.name}
            Email: {contact.email}
            Company: {contact.company}
            Subject: {contact.subject}
            
            Message:
            {contact.message}
            
            Submitted by user: {request.user.username}
            '''
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['sabkabaap060@gmail.com'],  # Your email
                fail_silently=False,
            )
            
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'OMNEXIA_APP/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'OMNEXIA_APP/contact_success.html')
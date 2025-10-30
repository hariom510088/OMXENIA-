from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    SERVICE_TYPES = [
        ('AI', 'AI & Machine Learning'),
        ('WEB', 'Web & App Development'),
        ('CLOUD', 'Cloud & DevOps'),
        ('SOFTWARE', 'Software Product Development'),
        ('CYBER', 'Cybersecurity & Automation'),
        ('DATA', 'Data Analytics & BI'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    icon = models.CharField(max_length=100, default='fas fa-cog')
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100, default='product.jpg')
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.CharField(max_length=100, default='team.jpg')
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='project.jpg')
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

class JobOpening(models.Model):
    JOB_TYPES = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('INTERNSHIP', 'Internship'),
        ('REMOTE', 'Remote'),
    ]
    
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    description = models.TextField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    applicant_phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"
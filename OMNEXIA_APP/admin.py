from django.contrib import admin
from .models import Service, Product, TeamMember, Contact, Project, JobOpening, JobApplication
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'featured')
    list_filter = ('service_type', 'featured')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'company', 'subject', 'message', 'created_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'is_active', 'posted_date')
    list_filter = ('department', 'job_type', 'is_active', 'posted_date')
    list_editable = ('is_active',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'applicant_email', 'job', 'applied_date')
    list_filter = ('applied_date', 'job')
    readonly_fields = ('applicant_name', 'applicant_email', 'applicant_phone', 'cover_letter', 'applied_date')
    
    def save_model(self, request, obj, form, change):
        # Send email notification when a new application is received
        if not change:  # Only for new applications
            subject = f'New Job Application: {obj.job.title}'
            message = f'''
            New job application received:
            
            Position: {obj.job.title}
            Applicant: {obj.applicant_name}
            Email: {obj.applicant_email}
            Phone: {obj.applicant_phone}
            
            Cover Letter:
            {obj.cover_letter}
            
            Please check the admin panel for more details.
            '''
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['sabkabaap060@gmail.com'],  # HR email
                fail_silently=False,
            )
        super().save_model(request, obj, form, change)

admin.site.site_header = "OMNEXIA GLOBAL TECHNOLOGY Admin"
admin.site.site_title = "OMNEXIA Admin Portal"
admin.site.index_title = "Welcome to OMNEXIA Admin Portal"
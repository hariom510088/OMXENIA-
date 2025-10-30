from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('solutions/', views.solutions, name='solutions'),
    path('products/', views.products, name='products'),
    path('projects/', views.projects, name='projects'),
    path('careers/', views.careers, name='careers'),
    path('careers/job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"
    
class about(models.Model):
    vision = models.TextField(blank=True, null=True) 
    overview = models.TextField(blank=True, null=True)   

    service_1_name = models.CharField(max_length=255, blank=True, null=True)
    service_1 = models.TextField(blank=True, null=True) 

    service_2_name = models.CharField(max_length=255, blank=True, null=True)
    service_2 = models.TextField(blank=True, null=True)

    service_3_name = models.CharField(max_length=255, blank=True, null=True) 
    service_3 = models.TextField(blank=True, null=True) 

    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Last updated {self.updated}"
    
    
class WhatWeOffer(models.Model):
    service_1_name = models.CharField(max_length=255, blank=True, null=True)
    service_1 = models.TextField(blank=True, null=True) 

    service_2_name = models.CharField(max_length=255, blank=True, null=True)
    service_2 = models.TextField(blank=True, null=True)

    service_3_name = models.CharField(max_length=255, blank=True, null=True) 
    service_3 = models.TextField(blank=True, null=True) 

    service_4_name = models.CharField(max_length=255, blank=True, null=True)
    service_4 = models.TextField(blank=True, null=True) 

    service_5_name = models.CharField(max_length=255, blank=True, null=True)
    service_5 = models.TextField(blank=True, null=True)

    service_6_name = models.CharField(max_length=255, blank=True, null=True) 
    service_6 = models.TextField(blank=True, null=True) 

    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Last updated {self.updated}"


class GetQuote(models.Model):
    SERVICE_CHOICES = [
        ('Software Engineering', 'Software Engineering'),
        ('SCRUM Framework', 'SCRUM Framework'),
        ('Website Design & Development', 'Website Design & Development'),
        ('Mobile Applications Development', 'Mobile Applications Development'),
        ('Mobile Wallet Development', 'Mobile Wallet Development'),
        ('ICT Consultancy', 'ICT Consultancy'),
        ('Payments Integration', 'Payments Integration'),
        ('Cloud Applications', 'Cloud Applications'),
        ('Software Support', 'Software Support'),
        ('Business Process Re-engineering', 'Business Process Re-engineering'),
    ]

    full_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    service_of_inquiry = models.CharField(max_length=150, choices=SERVICE_CHOICES)
    further_information = models.TextField(blank=True, null=True)
    date_of_inquiry = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - Date of Inquiry: {self.date_of_inquiry}"
    

class GetQuoteAssuarance(models.Model):    
    assuarance = models.TextField(null=True, blank=True)
    
class stayUpdated(models.Model):
    email = models.EmailField()    

    def __str__(self):
        return f"{self.email}"
    
class GetInTouch(models.Model):
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.email}"

class FollowUs(models.Model):
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.updated}"
    

class ContactRequest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Contact Request from {self.name} on {self.date.strftime('%Y-%m-%d')}"    
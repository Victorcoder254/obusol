from django.shortcuts import render
from .models import*
# Create your views here.

def home_view(request):
    # Fetch the latest data from the models
    about_info = about.objects.last()
    offers_info = WhatWeOffer.objects.last()
    follow_us_info = FollowUs.objects.last()
    get_in_touch_info = GetInTouch.objects.last()
    assurance_info = GetQuoteAssuarance.objects.last()

    # Define service choices for the GetQuote form
    service_choices = GetQuote.SERVICE_CHOICES

    # Handle POST requests for form submissions
    if request.method == "POST":
        # Handling GetQuote form submission
        if 'get_quote_form' in request.POST:
            full_name = request.POST.get("full_name")
            email_address = request.POST.get("email_address")
            service_of_inquiry = request.POST.get("service_of_inquiry")
            further_information = request.POST.get("further_information")

            GetQuote.objects.create(
                full_name=full_name,
                email_address=email_address,
                service_of_inquiry=service_of_inquiry,
                further_information=further_information
            )

        # Handling stayUpdated form submission
        elif 'stay_updated_form' in request.POST:
            email = request.POST.get("email")
            stayUpdated.objects.create(
                email=email
            )

        # Handling ContactRequest form submission
        elif 'contact_request_form' in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")

            ContactRequest.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

    # Add data to the context
    context = {
        'about_info': about_info,
        'offers_info': offers_info,
        'follow_us_info': follow_us_info,
        'get_in_touch_info': get_in_touch_info,
        'assurance_info': assurance_info,
        'service_choices': service_choices,  # Add choices to context
    }

    return render(request, 'files/index.html', context)

def admin_dashboard(request):
    get_quotes = GetQuote.objects.all().order_by('-date_of_inquiry')
    contact_requests = ContactRequest.objects.all().order_by('-date')
    stay_updated = stayUpdated.objects.all()
    # Add data to the context
    context = {
        'get_quotes': get_quotes,
        'contact_requests': contact_requests,
        'stay_updated': stay_updated, # Add choices to context
    }

    return render(request, 'files/admin_user.html', context)
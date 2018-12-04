from django.shortcuts import render
from .models import Events

# Create your views here.
def home(request):
    data = Events.objects.all()[:5]
    context = {
        'get_Data': data
    }
    home_template = 'ravens_consulting/home.html'
    return render(request, home_template, context)

def about(request):
    about_template = 'ravens_consulting/about.html'
    return render(request, about_template)

def contact(request):
    contact_template = 'ravens_consulting/contact.html'
    return render(request, contact_template)

def events(request):

    myEvent = Events.objects.all()
    context = {
        'site_heading': 'Our Events',
        'getData': myEvent
    }
    events_template = 'ravens_consulting/events.html'
    return render(request, events_template, context)

def ict(request):
    service_ict_template = 'ravens_consulting/services/ict.html'
    return render(request, service_ict_template)

def research(request):
    service_research_template = 'ravens_consulting/services/research.html'
    return render(request, service_research_template)
    
def publication(request):
    publication_template = 'ravens_consulting/publication.html'
    return render(request, publication_template)

def details(request, id):
    full_details = Events.objects.get(id = id)
    context = {
        'myEventDetails': full_details
    }
    details_template = 'ravens_consulting/details.html'
    return render(request, details_template, context)
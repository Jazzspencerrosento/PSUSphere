from django.shortcuts import render
from django.views.generic.list import ListView    
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization              # ← fetch all records from Organization table
    context_object_name = 'home'   # ← in the template: {{ home }} = the data
    template_name = "home.html"     # ← use this HTML file to display the page


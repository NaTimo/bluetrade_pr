from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Ad

def ads(request):
    ads = Ad.objects.all()
    context = {
        "ads": ads,
    }
    return render(request, "home.html", context=context)

# Create your views here.

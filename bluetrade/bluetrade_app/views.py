from django.shortcuts import render, get_object_or_404
from .models import Ad

def ads(request):
    ads = Ad.objects.all()
    context = {
        "ads": ads,
    }
    return render(request, "home.html", context=context)

def ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    context = {
        "ad": ad,
    }
    return render(request, "ad.html", context=context)

# Create your views here.

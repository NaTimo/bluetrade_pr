from django.shortcuts import render, get_object_or_404
from .models import Ad
from django.views import generic

def ads(request):
    ads = Ad.objects.all()
    peginate_by = 10
    context = {
        "ads": ads,
    }
    return render(request, "home.html", context=context)

class AdListView(generic.ListView):
    model = Ad
    template_name = "home.html"
    context_object_name = "ads"
def ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    context = {
        "ad": ad,
    }
    return render(request, "ad.html", context=context)

# Create your views here.

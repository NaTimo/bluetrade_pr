from django.shortcuts import render, get_object_or_404
from .models import Ad
from django.views import generic
from django.db.models import Q

class AdListView(generic.ListView):
    model = Ad
    paginate_by = 5
    template_name = "home.html"
    context_object_name = "ads"
def ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    context = {
        "ad": ad,
    }
    return render(request, "ad.html", context=context)

def search(request):
    query = request.GET.get("query")
    search_results = Ad.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    context = {
        "ads": search_results,
        "query": query,
    }
    return render(request, "search.html", context=context)
# Create your views here.

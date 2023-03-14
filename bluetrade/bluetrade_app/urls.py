
from django.urls import path
from . import views

urlpatterns = [
    path('<int:ad_id>/', views.ad, name='ad'),
    path("", views.AdListView.as_view(), name="home"),
    path("search/", views.search, name="search")
]
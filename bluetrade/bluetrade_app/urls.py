
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ads, name='home'),
    path('<int:ad_id>/', views.ad, name='ad'),
    path("", views.AdListView.as_view(), name="home")
]
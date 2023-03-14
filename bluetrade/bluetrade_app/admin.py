from django.contrib import admin
from .models import City, Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "due_ad_end", "display_city", "uuid")
    list_filter = ("title", "created_at", "due_ad_end", "city")
    search_fields = ("title", "uuid")

admin.site.register(City)
admin.site.register(Ad, AdAdmin)
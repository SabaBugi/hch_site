from django.contrib import admin
from .models import Service, SiteSettings, Goal

admin.site.register(Service)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_title", "hero_background"),
        }),
        ("About Section", {
            "fields": ("about_text",),
        }),
        ("Contact Information", {
            "fields": ("phone", "email", "address"),
        }),
    )

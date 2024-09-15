from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TravelPackage, Activity,TeamMember,TravelItinerary,ItineraryImage

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'review_rating', 'reviews_count')
    filter_horizontal = ('activities',)  # For better ManyToMany field representation

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ItineraryImageInline(admin.TabularInline):
    model = ItineraryImage
    extra = 1

@admin.register(TravelItinerary)
class TravelItineraryAdmin(admin.ModelAdmin):
    inlines = [ItineraryImageInline]



@admin.register(ItineraryImage)
class ItineraryImageAdmin(admin.ModelAdmin):
    pass

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import TravelPackage, Activity,TeamMember

def home(request):
    # Fetch featured packages and activities
    featured_packages = TravelPackage.objects.all()[:4]  # Top 3 packages
    featured_activities = Activity.objects.all()[:4]
    team_members=TeamMember.objects.all()# Top 3 activities
    context = {
        'featured_packages': featured_packages,
        'featured_activities': featured_activities,
        'team_members':team_members

    }
    return render(request, 'home/home.html', context)

def packages_list(request):
    packages = TravelPackage.objects.all()
    context = {'packages': packages}
    return render(request, 'home/packages_list.html', context)

def activities_list(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'home/activities_list.html', context)

def about_us(request):
    return render(request, 'home/about_us.html')

def travel_package_detail(request, pk):
    travel_package = TravelPackage.objects.get(pk=pk)
    return render(request, 'home/travel_package_detail.html', {'travel_package': travel_package})



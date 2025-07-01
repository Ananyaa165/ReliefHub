from django.shortcuts import render
from camp_details.models import CampDetails
# Create your views here.
def camp(request):
    if request.method=="POST":
        obj=CampDetails()
        obj.camp_name=request.POST.get('name')
        obj.location=request.POST.get('location')
        obj.no_of_refugees=request.POST.get('number')
        obj.no_of_volunteers=request.POST.get('numbers')
        obj.save()
    return render(request, 'camp_details/camp.html')
def camp_details(request):
    obj=CampDetails.objects.all()
    context={
        'o':obj
    }
    return render(request, 'camp_details/view_camp_details.html',context)
def view_camp_admin(request):
    obj=CampDetails.objects.all()
    context={
        'o':obj
    }
    return render(request, 'camp_details/view_camp_admin.html',context)
def view_camp_public(request):
    obj=CampDetails.objects.all()
    context={
        'o':obj
    }
    return render(request, 'camp_details/view_camp_public.html',context)

from django.shortcuts import render
from volunteer_activities.models import VolunteerActivites
from volunteer_reg.models import VolunteerReg
# Create your views here.
def volunteer_activities(request):
    ss=request.session["u_id"]
    if request.method=="POST":
        obj=VolunteerActivites()
        obj.activity=request.POST.get('update')
        obj.volunteer_id=ss
        obj.save()
    return render(request,'volunteer_activities/volunteer_activites_updation.html')


def view_volunteer_activities(request):
    obj=VolunteerActivites.objects.all()
    context={
        'o':obj
    }
    return render(request, 'volunteer_activities/view_volunteer_activities.html',context)

def view_volunteer_activities_public(request):
    obj=VolunteerActivites.objects.all()
    context={
        'o':obj
    }
    return render(request, 'volunteer_activities/view_volunteer_activity_public.html',context)

from django.shortcuts import render
from scheduling.models import Scheduling
from  camp_details.models import  CampDetails
from volunteer_reg.models import VolunteerReg
# Create your views here.
def scheduling(request,idd):
    ss=request.session["u_id"]
    if request.method=="POST":
        obj=Scheduling()
        obj.scheduled_task=request.POST.get('activity')
        obj.volunteer_id=idd
        obj.date=request.POST.get('date')
        obj.save()
        return scheduling_activities(request)
    return render(request,'scheduling/scheduling_admin.html')

def scheduling_activities(request):
    obj=VolunteerReg.objects.all()
    context={
        'o':obj
    }
    return render(request,'scheduling/scheduling_volunteer_activities.html',context)
def scheduling_view(request):
    ss = request.session["u_id"]
    obj = Scheduling.objects.filter(volunteer_id=ss)
    context={
        'o':obj
    }
    return render(request,'scheduling/view_volunteer_scheduling.html',context)

def admin_task_view(request):
    obj=Scheduling.objects.all()
    context={
        'o':obj
    }
    return render(request,'scheduling/admin_task_view.html',context)

def delete(request,idd):
    obj=Scheduling(task_id=idd)
    obj.delete()
    return admin_task_view(request)

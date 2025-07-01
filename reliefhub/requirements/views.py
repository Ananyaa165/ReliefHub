from django.shortcuts import render
from requirements.models import Requirements
from camp_details.models import CampDetails
from volunteer_reg.models import VolunteerReg
from delivery.models import Delivery
# Create your views here.
def requirements(request):
    ss=request.session["u_id"]
    ob = CampDetails.objects.all()
    context = {
        'a': ob,
    }
    if request.method=="POST":
        obj=Requirements()
        obj.requirements=request.POST.get('requirements')
        obj.quantity=request.POST.get('quantitys')
        obj.camp_id=request.POST.get('camp')
        obj.volunteer_id=ss
        obj.delivery_id=1
        obj.save()
    return render(request,'requirements/requirements_post.html',context)
def requirements_view(request):
    obj=Requirements.objects.all()
    context={
        'o':obj
    }
    return render(request,'requirements/view_requirements.html',context)

def requirements_manage(request):
    obj=Requirements.objects.all()
    context={
        'o':obj
    }
    return render(request,'requirements/manage_requiremnt.html',context)

def delete(request,idd):
    obj=Requirements(requirement_id=idd)
    obj.delete()
    return requirements_manage(request)
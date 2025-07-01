from django.shortcuts import render
from volunteer_reg.models import VolunteerReg
from login.models import Login
from camp_details.models import CampDetails
from django.core.files.storage import FileSystemStorage
# Create your views here.
def mng_volunteer(request):
    obj=VolunteerReg.objects.all()
    context={
        'o':obj
    }
    return render(request,'volunteer_reg/manage_volunteer.html',context)
def volunteer_reg(request):
    ob = CampDetails.objects.all()

    txt=""
    if request.method=="POST":
        obj = VolunteerReg()
        obj.volunteer_name=request.POST.get('name')
        obj.designation=request.POST.get('designation')
        obj.email_id = request.POST.get('email')
        obj.camp_id=request.POST.get('camp')
        obj.volunteer_ph=request.POST.get('number')
        obj.skill=request.POST.get('skill')
        obj.document=1
        myfile = request.FILES['upload']
        fs = FileSystemStorage()
        fs.save(myfile.name,myfile)
        obj.document=myfile.name
        obj.availability=request.POST.get('availability')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('radio')
        obj.address=request.POST.get('address')
        obj.user_name=request.POST.get('username')
        obj.password=request.POST.get('psw')
        obj.status='pending'
        obj.save()

        txt="Registered Successfully"
    context={
            'msg':txt,
        'a':ob

        }
    return render(request,'volunteer_reg/volunteer_reg.html',context)

def approve(request,idd):
    obj=VolunteerReg.objects.get(volunteer_id=idd)
    obj.status="Approved"
    obj.save()
    ob = Login()
    ob.username = obj.email_id
    ob.password = obj.password
    ob.type = "volunteer"
    ob.u_id = obj.volunteer_id
    ob.save()

    return mng_volunteer(request)
def rejected(request,idd):
    obj=VolunteerReg.objects.get(volunteer_id=idd)
    obj.status="rejected"
    obj.save()
    return mng_volunteer(request)
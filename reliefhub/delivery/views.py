from django.shortcuts import render
from delivery.models import Delivery
from camp_details.models import CampDetails
from public_reg.models import PublicReg
from requirements.models import Requirements
# Create your views here.
def delivery(request):
    ss=request.session["u_id"]
    ob=CampDetails.objects.all()
    obb=PublicReg.objects.all()
    obbb=Requirements.objects.all()
    context={
        'a':ob,
        'b':obbb

    }
    if request.method=="POST":
        obj=Delivery()
        obj.camp_id=request.POST.get('camp')
        obj.volunteer_id=ss
        obj.item=request.POST.get('item')
        obj.phone_no=request.POST.get('phone_no')
        obj.quantity_c=request.POST.get('quantity')
        obj.public_location=request.POST.get('location')
        obj.public_id=request.POST.get('public')
        obj.status='collected'
        obj.save()
    return render(request,'delivery/collected_goods.html',context)
def delivery_collection(request):
    obj=Delivery.objects.all()
    context={
        'o':obj
    }
    return render(request,'delivery/collection_and_delivery.html',context)

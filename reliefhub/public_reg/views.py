from django.shortcuts import render
from public_reg.models import PublicReg
from login.models import Login
# Create your views here.
def public_reg(request):
    txt=""
    if request.method=="POST":
        obj=PublicReg()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.phone_no=request.POST.get('phone_no')
        obj.user_name=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.email=request.POST.get('email')
        obj.save()

        ob = Login()
        ob.username = obj.user_name
        ob.password = obj.password
        ob.type = "public"
        ob.u_id = obj.public_id
        ob.save()
        txt="Registered SuccessFully"
    context = {
            'msg': txt
        }
    return render(request,'public_reg/public_reg.html',context)
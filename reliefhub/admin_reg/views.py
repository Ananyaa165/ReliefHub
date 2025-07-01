from django.shortcuts import render
from admin_reg.models import AdminReg
from login.models import Login

# Create your views here.
def admin_reg(request):
    txt=""
    if request.method=="POST":
        obj=AdminReg()
        obj.admin_name=request.POST.get('name')
        obj.contact_no=request.POST.get('contact')
        obj.designation=request.POST.get('designation')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.user_name=request.POST.get('username')
        obj.save()

        # ob = Login()
        # ob.username = obj.email
        # ob.password = obj.password
        # ob.type = "admin"
        # ob.u_id = obj.admin_id
        # ob.save()

        txt = "Registered Successfully"
        context = {
            'msg': txt,

        }
        return render(request, 'admin_reg/admin_reg.html', context)

    return render(request,'admin_reg/admin_reg.html')
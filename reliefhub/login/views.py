from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.
def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pswd=request.POST.get('psw')
        obj = Login.objects.filter(username=name,password=pswd)
        for ob in obj:

            if ob.username==name and ob.password==pswd:
                type=ob.type
                uid=ob.u_id
                if type=="admin":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/admin/')
                elif type=="volunteer":
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/volunteer/')
                elif type=="public":
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/public/')
            else:
                alert = "Invalid Username or Password "
                context = {
                    'msg': alert
                }
        else:
            alert="Invalid Username or Password "
            context={
                'msg':alert
            }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')

import smtplib

def forget_password(request):
    email = "projectmailbg@gmail.com"
    if request.method=="POST":
        em=request.POST.get('email')
        if Login.objects.filter(username=em).exists():
            ob=Login.objects.get(username=em)
            pwd=ob.password
            sub = "Forget Password"
            msg = 'Username:'+em+'& Password: '+pwd
            text = f'subject :{sub}\n\n{msg}'
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, 'iqjjrhsyerovorav')
            server.sendmail(email, str(em), text)
        else:
            message="Invalid Username"
            context={
                'msg':message
            }
            return render(request, 'login/forget.html',context)
    return render(request,'login/forget.html')
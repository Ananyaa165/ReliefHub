from django.shortcuts import render
from public_reg.models import PublicReg
from chat.models import Chat
import datetime
from django.db.models import Q
from scheduling.models import Scheduling
# Create your views here.
from login.models import Login


def con(request):
    ob= Scheduling.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session["u_id"]
    obj = Scheduling.objects.get(task_id=idd)
    ob = Chat.objects.filter(Q(public_id=ss) & Q(task_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.task_id=idd
        obk.public_id=ss
        obk.rectype="volunteer"
        obk.sendertype = "public"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ob=PublicReg.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =PublicReg.objects.get(public_id=idd)
    ob=Chat.objects.filter(Q(public_id=idd) & Q(task_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.public_id=idd
        obk.task_id=ss
        obk.rectype="public"
        obk.sendertype="volunteer"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)

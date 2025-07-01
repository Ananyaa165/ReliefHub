from django.shortcuts import render
from notification.models import Notification
import datetime
# Create your views here.
def notification(request):
    if request.method=="POST":
        obj=Notification()
        obj.notification=request.POST.get('notification')
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.admin_id=1
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')
def notification_view(request):
    obj=Notification.objects.all()
    context={
        'o':obj
    }
    return render(request,'notification/view_notification.html',context)

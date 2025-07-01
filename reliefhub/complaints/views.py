from django.shortcuts import render
from complaints.models import Complaints
# Create your views here.
def complaints(request):
    ss=request.session["u_id"]
    if request.method=="POST":
        obj=Complaints()
        obj.volunteer_id=ss
        obj.complaint = request.POST.get('complaints')
        obj.reply='pending'
        obj.save()
    return render(request,'complaints/complaints.html')

def complaints_reply(request,idd):
    if request.method=="POST":
        obj=Complaints.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        return complaints_admin(request)
    return render(request, 'complaints/reply.html')

def complaints_admin(request):
    obj=Complaints.objects.all()
    context={
        'o':obj
    }
    return render(request, 'complaints/view_complaint_adm.html',context)
def complaints_view(request):
    ss=request.session["u_id"]
    obj=Complaints.objects.filter(volunteer_id=ss)
    context={
        'o':obj
    }
    return render(request, 'complaints/view_reply.html',context)
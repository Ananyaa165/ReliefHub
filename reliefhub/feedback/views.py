from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def feedback(request):
    ss=request.session["u_id"]
    if request.method=="POST":
        obj=Feedback()
        obj.feedback=request.POST.get('feedback')
        obj.public_id=ss
        obj.date=datetime.datetime.today()
        obj.save()
    return render(request,'feedback/feedback.html')

def feeback_view(request):
    obj=Feedback.objects.all()
    context={
        'o':obj
    }
    return render(request,'feedback/view_feedback.html',context)
def feedback_view_volunteer(request):
    obj=Feedback.objects.all()
    context={
        'o':obj
    }
    return render(request,'feedback/view_feedback_volunteer.html',context)
def feedback_view_public(request):
    obj=Feedback.objects.all()
    context={
        'o':obj
    }
    return render(request,'feedback/view_feedback_public.html',context)

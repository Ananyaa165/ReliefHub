from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')
def volunteer(request):
    return render(request,'temp/volunteer.html')
def home(request):
    return render(request,'temp/home.html')
def public(request):
    return render(request,'temp/public.html')
def adminbase(request):
    return render(request, 'temp/homebase.html')
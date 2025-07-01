"""reliefhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('admin_reg/', include('admin_reg.url')),
    url('camp_details/', include('camp_details.url')),
    url('chat/', include('chat.url')),
    url('complaint/', include('complaints.url')),
    url('delivery/', include('delivery.url')),
    url('feedback/', include('feedback.url')),
    url('login/', include('login.url')),
    url('notification/', include('notification.url')),
    url('public_reg/', include('public_reg.url')),
    url('requirements/', include('requirements.url')),
    url('scheduling/', include('scheduling.url')),
    url('volunteer_activities/', include('volunteer_activities.url')),
    url('volunteer_reg/', include('volunteer_reg.url')),
    url('temp/',include('temp.url')),
    url('$',views.home)



]

from django.conf.urls import url
from temp import views

urlpatterns=[
    url('admin/',views.admin),
    url('volunteer/',views.volunteer),
    url('home/',views.home),
    url('public/',views.public),
    url('adminbase/',views.adminbase),
]
from django.conf.urls import url
from volunteer_reg import views
urlpatterns=[
    url('mng_volunteer/', views.mng_volunteer),
    url('volunteer_reg/', views.volunteer_reg),
    url('approve/(?P<idd>\w+)',views.approve),
    url('rejected/(?P<idd>\w+)',views.rejected),
]
from django.conf.urls import url
from complaints import views

urlpatterns=[
    url('complaints/',views.complaints),
    url('reply/(?P<idd>\w+)',views.complaints_reply),
    url('complaints_admin/',views.complaints_admin),
    url('complaints_view/',views.complaints_view)

]

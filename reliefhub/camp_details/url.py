from django.conf.urls import url
from camp_details import views

urlpatterns=[
    url('camp/',views.camp),
    url('camp_details/',views.camp_details),
    url('view_camp_admin/',views.view_camp_admin),
    url('viwpublic/',views.view_camp_public)
]
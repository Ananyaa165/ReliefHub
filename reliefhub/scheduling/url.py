from django.conf.urls import url
from scheduling import views

urlpatterns=[
    url('schedulng/(?P<idd>\w+)',views.scheduling),
    url('scheduling_activities/',views.scheduling_activities),
    url('view_scheduling/',views.scheduling_view),
    url('view_admin/',views.admin_task_view),
    url('delete/(?P<idd>\w+)', views.delete),
]
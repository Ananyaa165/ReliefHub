from django.conf.urls import url
from volunteer_activities import views
urlpatterns=[
    url('volunteer_activities/',views.volunteer_activities),
    url('volunteer_activities_updation/', views.view_volunteer_activities),
    url('volunteer_activity_public/',views.view_volunteer_activities_public),
]
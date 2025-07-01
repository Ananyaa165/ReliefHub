from django.conf.urls import url
from feedback import views
urlpatterns=[
    url('feedback/',views.feedback),
    url('feeback_view/',views.feeback_view),
    url('feedback_view_volunteer/',views.feedback_view_volunteer),
    url('feedback_view_public/',views.feedback_view_public),
]
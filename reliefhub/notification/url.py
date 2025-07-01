from django.conf.urls import url
from notification import views
urlpatterns=[
    url('notification/',views.notification),
    url('notification_view/',views.notification_view)
]
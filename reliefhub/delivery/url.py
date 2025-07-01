from django.conf.urls import url
from delivery import views
urlpatterns=[
    url('delivery/',views.delivery),
    url('delivery_collection/',views.delivery_collection)
]
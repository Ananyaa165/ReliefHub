from django.conf.urls import url
from public_reg import views
urlpatterns=[
    url('public_reg/',views.public_reg)
]
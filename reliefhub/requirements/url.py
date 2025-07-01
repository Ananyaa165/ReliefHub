from django.conf.urls import url
from requirements import views
urlpatterns=[
    url('requirements/',views.requirements),
    url('requirements_view/',views.requirements_view),
    url('manage/',views.requirements_manage),
    url('delete/(?P<idd>\w+)',views.delete),
]

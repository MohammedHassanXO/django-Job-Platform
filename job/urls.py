from django.urls import path
from .views import job_list, job_detail
urlpatterns = [
    path('', job_list),
     path('<slug:slug>', job_detail),
]
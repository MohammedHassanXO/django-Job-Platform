from django.urls import path
from .views import job_list, job_detail, JobApply
from .api import JobListAPI, JobDetailAPI #job_list_api, job_detail_api
urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),
    path('<slug:slug>/apply', JobApply.as_view()),
    
    
    path('api/list/', JobListAPI.as_view()),
    path('api/list/<int:pk>', JobDetailAPI.as_view()),
]
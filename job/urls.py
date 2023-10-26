from django.urls import path
from .views import job_list, job_detail
from .api import job_list_api, job_detail_api
urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),
    
    
    path('api/list', job_list_api),
    path('api/list/<int:id>', job_detail_api),
]
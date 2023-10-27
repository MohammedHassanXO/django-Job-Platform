from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import JobSerializers
from .models import Job

'''
@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    data = JobSerializers(jobs, many=True).data
    return Response({'jobs':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job = Job.objects.get(id=id)
    data = JobSerializers(job).data
    return Response({'job':data})
'''

class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    
class JobDetailAPI(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    
    
    
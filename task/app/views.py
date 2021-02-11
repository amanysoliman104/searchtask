from django.shortcuts import render
from .models import Coffee_Machine , Coffee_Pod
from .filters import MachineFilter ,PodFilter 
# Create your views here.
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
#from .serializers import Coffee_Machine_Serializer , Coffee_Pod_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
#from app.models import Coffee_Machine , Coffee_Pod


"""@api_view(['GET', 'POST'])
def coffee_machine_list(request):
    if request.method == 'GET':
        machine_list = Coffee_Machine.objects.all()

        machine_type = request.GET.get('machine_type', None)
        if machine_type is not None:
            machine_list = machine_list.filter(machine_type__icontains=machine_type)
         
        machine_serializer = Coffee_Machine_Serializer(machine_list, many=True)
        return JsonResponse(machine_serializer.data, safe=False)

    

@api_view(['GET', 'POST'])
def coffee_pod_list(request):
    if request.method == 'GET':
        pod_list = Coffee_Pod.objects.all()
        
    
    pod_serializer = Coffee_Pod_Serializer(pod_list, many=True)
    return JsonResponse(pod_serializer.data, safe=False)
    """


def home(request):
    return render(request,"home.html","")


def machine_list(request):
    mfilter = MachineFilter(request.GET, queryset=Coffee_Machine.objects.all())
    
    return render(request, 'machine_list.html', {'filter': mfilter})
            


        
     

def pod_list(request):
    pfilter = PodFilter(request.GET, queryset=Coffee_Pod.objects.all())
    
    return render(request, 'pod_list.html', {'filter': pfilter})
            

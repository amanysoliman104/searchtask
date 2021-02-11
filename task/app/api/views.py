import django_filters.rest_framework
import django_filters 
from django.shortcuts import render
from app.models import Coffee_Machine , Coffee_Pod

# Create your views here.
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from app.serializers import Coffee_Machine_Serializer , Coffee_Pod_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Coffee_Machine , Coffee_Pod


#***********************************************************

class CoffeeMachineAPIList(generics.ListAPIView):
    queryset = Coffee_Machine.objects.all()
    serializer_class = Coffee_Machine_Serializer
    permission_classes = [permissions.IsAuthenticated]

    
#************************************************************
class CoffeeMachineAPISearch(generics.ListAPIView):
    queryset = Coffee_Machine.objects.all()
    serializer_class=Coffee_Machine_Serializer 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields=('machine_type', 'water_line')

#************************************************************


#*************************************************************   

class CoffeePodAPIList(generics.ListAPIView):
    queryset = Coffee_Pod.objects.all()
    serializer_class = Coffee_Pod_Serializer
    permission_classes = [permissions.IsAuthenticated]
        
 #****************************************************************
class CoffeePodAPISearch(generics.ListAPIView):
    queryset = Coffee_Pod.objects.all()
    serializer_class=Coffee_Pod_Serializer 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields=('pod_type', 'flaver','pack_size')






"""  
 def get_queryset(self,*args,**kwargs):
        qs=Coffee_Machine.objects.all()
        
        query =self.kwargs["machinetype"]
        if query is not None:
            qs=qs.filter(machine_type=query) 
            codes=qs.get('code')
            return codes
        else:    
            return qs 

"""
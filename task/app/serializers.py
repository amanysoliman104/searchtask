from rest_framework import serializers 
from .models import Coffee_Machine , Coffee_Pod

class Coffee_Machine_Serializer(serializers.ModelSerializer):
  
    class Meta:
        model = Coffee_Machine
        fields = ('machine_type',
                  'water_line',
                  'code',
                  'model'
                  )
        

    
#*****************************************************************

class Coffee_Pod_Serializer(serializers.ModelSerializer):
 
    class Meta:
        model = Coffee_Pod
        fields = ('pod_type',
                  'flaver',
                  'pack_size',
                  'code')

    def get_display(self):
        return self.code
from django.db import models

class Coffee_Machine(models.Model):

    machine_type=models.CharField(max_length=120)
    water_line  =models.BooleanField()
    code        =models.CharField(max_length=120)
    model       =models.CharField(max_length=120)



    def __str__(self):
        return self.code 
 

#******************************************************#
class Coffee_Pod(models.Model):
    pod_type   =models.CharField(max_length=120)
    flaver      =models.CharField(max_length=120)
    pack_size   =models.CharField(max_length=120)
    code        =models.CharField(max_length=120)
    

    def __str__(self):
        return self.code 
   

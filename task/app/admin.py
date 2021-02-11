from django.contrib import admin

# Register your models here.
from .models import Coffee_Machine , Coffee_Pod
admin.site.register(Coffee_Machine)
admin.site.register(Coffee_Pod)

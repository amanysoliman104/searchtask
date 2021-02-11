import django_filters
from .models import Coffee_Machine , Coffee_Pod

class MachineFilter(django_filters.FilterSet):
    #code= django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Coffee_Machine
        fields = ['machine_type', 'water_line']



#**********************************************************************

class PodFilter(django_filters.FilterSet):
    #code= django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Coffee_Pod
        fields = ['pod_type','flaver' ,'pack_size']
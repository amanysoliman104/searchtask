from django.conf.urls import url 
from app.views import machine_list ,pod_list
from app.api.views  import ( 
	CoffeeMachineAPIList , 
	CoffeePodAPIList , 
	CoffeeMachineAPISearch,
	CoffeePodAPISearch,
	)

urlpatterns = [ 
    url(r'^machine$',machine_list),
    url(r'^pod$',pod_list),
    url(r'^api/machine$', CoffeeMachineAPIList.as_view()),
    url(r'^api/pods$', CoffeePodAPIList.as_view()),
    url(r'^api/search/machine/', CoffeeMachineAPISearch.as_view()),
    url(r'^api/search/pods/', CoffeePodAPISearch.as_view()),
    
]

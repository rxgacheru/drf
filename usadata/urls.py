from django.urls import path
from usadata.views import *

urlpatterns = [
    path('api/states', StateList.as_view, name = 'state-List'),
    path('api/states/<int:id>/', StateDetail.as_view(), name = 'state-detail'),
    path('people/', PersonList.as_view(), name='person.list'),
    path('people/<int:pk>/', PersonDetail.as_view(), name= 'person-detail')
]

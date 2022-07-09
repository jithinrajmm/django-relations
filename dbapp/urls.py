from django.urls import path
from dbapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:pk>/',views.PersonIntrest.as_view(),name='detail'),
    path('personaddress/',views.PersonAddress.as_view(),name='person_address'),
    path('personfromcities/',views.PersonsFromCities.as_view(),name='perosns_from_city'),
    path('intrestPersons/',views.IntrestsPersonss.as_view(),name = 'intresttomanyPersons'),
    
    
]
from django.contrib import admin
from dbapp.models import Person,PersonAddress,Intrests,City

# Register your models here.

admin.site.register(PersonAddress)
admin.site.register(Person)
admin.site.register(Intrests)
admin.site.register(City)

# this is the another way to register our database to admin pannel
# admin.site.register([Person,PersonAddress,Intrests,City])
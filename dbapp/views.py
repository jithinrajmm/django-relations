from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from dbapp.models import Person,PersonAddress,City,Intrests
from django.views.generic import DetailView



# class HomeView(View):
#     def get(self,request,*args,**kwargs):
        
#         context = {
            
#         }
#         return render(request,'home.html',context)

class HomeView(View):
    def get(self,request,*args,**kwargs):
        
        persons = Person.objects.all()
        for i in persons:
            print(i)
            
        person = Person.objects.get(pk=1)
        print('*'*100)
        print(person)
        intrest = person.intrest.all()
        for i in intrest:
            print(i.title,'---->', person.name)
    
        
        person = Person.objects.get(pk=2)
        print('*'*100)
        print(person)
        intrest = person.intrest.all()
        for i in intrest:
            print(i.title,'---->', person.name)
    
        
        person2 = Person.objects.get(pk=3)
        print('*'*100)
        print(person2.name)
        intrests = person2.intrest.all()
        for i in intrests:
            print(i.title,'--->',person2.name)
        print('*'*100)
        return render(request,'home.html')
        
home = HomeView.as_view()


class PersonAddress(View):
    def get(self,reqeust,*args,**kwargs):
        person = Person.objects.get(pk=2)
        # in the PersonAddress name models , its connected to the person with one to many relation
        # the we can acces its from person object like this
        # just lowercase of the database name of the model where the one to one is defined
        
        
        address = person.personaddress
        print(address.person.name)
        print(address.city)
        print(address.street_address)
        print(address,'addrss of the ',person.name)
        return render(reqeust, 'personaddress.html',{'address':address})

class PersonIntrest(DetailView):
    model = Person
    template_name = 'personintrest.html'
    
    # def get(self,request,*args,**kwargs):
    #     print(kwargs['pk'])
    #     return render(request,'personintrest.html')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['interests']
        return context

class IntrestsPersonss(View):
    ''' this is from the interst to the person relations '''
    def get(self,reqeust,*args,**kwargs):
        
        intrest = Intrests.objects.get(id=1)
        print(intrest)
        # i take one intrest from the intrest table and 
        # collcted all the person related to the purticular intrest
        persons = intrest.person_set.all()
        print(persons)
        
        # the pserson intrest also we can select from the person table
        person = Person.objects.get(id=2)
        single_person_intrest = person.intrest.all()
        print(person.name)
        print(single_person_intrest)
        
        
        return HttpResponse('haiii')
        
class PersonsFromCities(View):
    def get(self,request,*args,**kwargs):
        
        city = City.objects.get(id=3)
        print(city)
        all_addrss_from_single_city = city.personaddress_set.all()
        print(all_addrss_from_single_city)
        
        context = {
            
        }
        return render(request,'person_from_city.html')
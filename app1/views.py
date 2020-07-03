from django.shortcuts import render
from app1.serializers import Bankserializer
from rest_framework import generics
from .models import Branches


# Create your views here.

class BankDetails(generics.ListAPIView):
    serializer_class = Bankserializer

    def get_queryset(self):
        qs =Branches.objects.all()
        ifscno = self.request.GET.get('ifsc')
        bank_name = self.request.GET.get('bank')
        city = self.request.GET.get('city')
        if ifscno is not None:
            qs = qs.filter(ifsc__exact=ifscno)
        elif bank_name and city is not None:
            qs = qs.filter(bank_name__exact=bank_name).filter(city__exact=city)
        return qs

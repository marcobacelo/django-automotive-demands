from .models import Person
from .models import Demands
from .models import Contact

from rest_framework import viewsets
from .serializers import PersonSerializer
from .serializers import DemandsSerializer
from .serializers import ContactSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DemandsViewSet(viewsets.ModelViewSet):
    queryset = Demands.objects.all()
    serializer_class = DemandsSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

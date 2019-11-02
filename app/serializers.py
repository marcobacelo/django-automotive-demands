from .models import Person
from .models import Demands
from .models import Contact
from .models import Profile

from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('cpf', 'name', 'contact', Profile, 'demands')


class DemandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demands
        fields = ('description', 'receiver', 'status')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'address', 'celNumber')

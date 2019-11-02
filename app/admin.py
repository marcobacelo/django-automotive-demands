from django.contrib import admin
from .models import Person
from .models import Demands
from .models import Contact

admin.site.register(Person)
admin.site.register(Demands)
admin.site.register(Contact)

from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=75, primary_key=True)
    address = models.CharField(max_length=100)
    celNumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'contact'


class Profile(models.Model):
    profileName = models.CharField(max_length=10, primary_key=True)

    class Meta:
        db_table = 'profile'


class Demands(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=500)
    receiver = models.CharField(max_length=15)
    status = models.BooleanField(default=True, verbose_name='status')

    class Meta:
        db_table = 'demands'


class Person(models.Model):
    cpf = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100, db_column='name')
    profile = models.ForeignKey('Profile', to_field="profileName", on_delete=models.CASCADE)
    contact = models.OneToOneField('Contact', to_field='email', on_delete=models.CASCADE)
    demands = models.ManyToManyField(Demands, db_column='idDemands')

    class Meta:
        db_table = 'person'

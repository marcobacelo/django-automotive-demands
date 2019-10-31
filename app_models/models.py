from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=100)
    celNumber = models.CharField(max_length=20)


class Profile(models.Model):
    profileName = models.CharField(max_length=10)


class Demands(models.Model):
    id = models.IntegerField(models.AutoField(primary_key=True))
    description = models.TextField(max_length=300)
    receiver = models.CharField(max_length=15)
    idPerson = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='cpfPerson')


class Person(models.Model):
    cpf = models.IntegerField(primary_key=True, db_column='cpf')
    name = models.CharField(max_length=100, db_column='name')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, db_column='profile')
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, db_column='contact')
    demands = models.ManyToManyField(Demands, db_column='idDemands')

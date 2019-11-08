from django.db import models
from django.contrib.auth.models import User


class Demands(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=500, verbose_name='Descrição')
    destiny = models.CharField(max_length=50, verbose_name='Destinatário')
    status = models.BooleanField(default=True, verbose_name='Status')
    personalContact = models.ManyToManyField('UserDetails', verbose_name='Contato associado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'demands'


class UserDetails(models.Model):
    cpf = models.CharField(max_length=15, primary_key=True, verbose_name='CPF')
    name = models.CharField(max_length=100, db_column='name', verbose_name='Nome')
    cellphone = models.CharField(max_length=20, verbose_name='Celular')
    userId = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, verbose_name='Anunciantes')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_details'

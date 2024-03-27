from django.db import models
from django.contrib.auth.models import AbstractUser

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Hobby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Хобби'
        verbose_name_plural = 'Хобби'
    
class User(AbstractUser):
    patronymic = models.CharField('Отчество', max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    tel = models.IntegerField(null=True, blank=True)
    hobbys = models.ManyToManyField(to=Hobby, related_name='user_hobbies')

from django.db import models

# Create your models here.

class  Owner(models.Model):
    full_name = models.TextField(verbose_name="ФИО")
    avatar = models.FileField(verbose_name="Аватар")

    def __str__(self):
        return self.full_name

class Product(models.Model):
    name=models.CharField(max_length = 100, verbose_name = "Наименование")
    description = models.TextField(verbose_name = 'Описание ')
    cost = models.FloatField(verbose_name='Цена')
    rating = models.FloatField(verbose_name='Реййтинг')
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + ": "+ self.description

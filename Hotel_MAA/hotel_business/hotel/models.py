from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from datetime import datetime

#Верхние слева-------------------------------------------------------------------
class Passport(models.Model): #паспорт
    Documented = models.IntegerField(max_length=6)
    Series = models.IntegerField(max_length = 4)
    Number = models.IntegerField(max_length = 6)
    Day_of_Issue = models.DateTimeField()
    Issued_By =models.TextField(max_length = 255)

    def __str__(self):
        return  self.Documented

class Guest(models.Model):  # гость
    Guest_Id = models.CharField(max_length=6)
    First_name = models.CharField(max_length= 150)
    Name = models.CharField(max_length=150)
    Second_Name = models.CharField(max_length= 150)
    Number_phone = models.IntegerField(max_length=14)
    Date_Birth = models.DateTimeField()
    Document = models.ForeignKey(Passport, on_delete = models.CASCADE)
    Number = models.IntegerField(max_length=6)
    Day_of_Issue = models.DateTimeField()
    Issued_By = models.TextField(max_length=255)

    def __str__(self):
        return self.Guest_Id


#Середина слева-------------------------------------------------------------------
class Category(models.Model): #Категория
    Category_Id = models.IntegerField(max_length=6)
    Tittle = models.IntegerField(max_length = 250)
    Price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    Description =models.TextField(max_length = 555)

    def __str__(self):
        return  self.Category_Id

class Number(models.Model): #Номер
    Number_Id = models.IntegerField(max_length=6)
    Floor = models.DecimalField( max_digits = 3)
    Sum_Rooms = models.DecimalField( max_digits = 4)
    Sum_Beds = models.DecimalField(max_digits = 4)
    Category_Id =models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return  self.Number_Id

#слева снизу-------------------------------------------------------------------
class Subject(models.Model): #Предмет
    Subject_Id = models.IntegerField(max_length=6)
    Tittle = models.IntegerField(max_length = 250)

    def __str__(self):
        return self.Subject_Id

class Equipment(models.Model): #Оснащение
    Category_Id = models.ForeignKey(Category, on_delete = models.CASCADE)
    Subject_Id = models.ForeignKey(Subject, on_delete = models.CASCADE)

    def __str__(self):
        return self.Category_Id

#справа-------------------------------------------------------------------
class Service(models.Model): #Предмет
    Service_Id = models.IntegerField(max_length = 5)
    Tittle = models.IntegerField(max_length = 250)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(max_length=555)

    def __str__(self):
        return self.Service_Id

class Rendering(models.Model): #Предмет
    Rendering_ID = models.IntegerField(max_length = 5)
    Tittle = models.IntegerField(max_length = 250)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(max_length=555)

    def __str__(self):
        return self.Rendering_ID


class Rendering_Service(models.Model): #Предмет
    Ren_Service_Id = models.IntegerField(max_length = 5)
    Ren_Id = models.ForeignKey(Rendering, on_delete = models.CASCADE)
    Service_Id = models.ForeignKey(Service, on_delete = models.CASCADE)
    Quantity = models.IntegerField(max_length = 10)
    Day_pay_Product = models.DateTimeField()

    def __str__(self):
        return self.Ren_Service_Id

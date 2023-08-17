from django.db import models


class Restaurant(models.Model):
    objects = None
    name = models.CharField(max_length=100)


class Menu(models.Model):
    objects = None
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()


class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)


class Vote(models.Model):
    objects = None
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

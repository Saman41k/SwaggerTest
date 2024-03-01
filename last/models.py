from django.db import models


class Car(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    car_model = models.TextField()
    car_category = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
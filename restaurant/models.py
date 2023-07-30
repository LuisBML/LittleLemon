from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=255)
    no_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

    def __str__(self) -> str:
        return f'{self.title}: {self.price}'

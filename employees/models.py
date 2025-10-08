from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_hired = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

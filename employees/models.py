from django.db import models

<<<<<<< HEAD
class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name
=======
# Create your models here.
>>>>>>> 788edbefc1c769f095d238a38792afe77bf11b43

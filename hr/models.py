from django.db import models

# Create your models here.
class hooda(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    mobile_no = models.IntegerField()
    email = models.EmailField()

    # def __str__(self):
    #     return self.name

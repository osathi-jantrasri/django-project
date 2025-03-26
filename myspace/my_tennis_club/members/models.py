from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    note = models.CharField(max_length=100)
    bday = models.DateField()
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
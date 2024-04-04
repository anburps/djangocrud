from django.db import models

# Create your models here.
class CrudView(models.Model):
    name    =   models.CharField(max_length=200)
    email   =   models.EmailField()
    dob     =   models.DateField()
    address =   models.TextField()
    place   =   models.CharField(max_length=200)
    
    def __str__(self) :
        return self.name
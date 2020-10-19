from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=40, choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image = models.ImageField(upload_to='images/',blank = True)
    date_added = models.DateField(auto_now_add=True)
    
from django.db import models

class Details(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    birth=models.TextField()
    email=models.EmailField()
    p_number=models.TextField()
    location=models.TextField()
    Radio=models.TextField()



# Create your models here.

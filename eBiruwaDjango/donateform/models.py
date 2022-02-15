from django.db import models

# Create your models here.


class Donateform(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)

    class Meta:

        db_table = "alldonations"
        
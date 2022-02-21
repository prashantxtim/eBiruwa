from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        db_table = "user"
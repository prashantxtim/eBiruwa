from django.db import models

# Create your models here.
class Donor(models.Model):
    donor_id = models.AutoField(auto_created=True, primary_key=True)
    donor_username = models.CharField(max_length=200)
    donor_email = models.CharField(max_length=200)
    donor_password = models.CharField(max_length=200)

    class Meta:

        db_table = "donor"
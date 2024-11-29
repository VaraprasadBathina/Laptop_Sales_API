from django.db import models

# Create your models here.
from django.db import models

class SalesData(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    product = models.CharField(max_length=100)
    sale_amount = models.FloatField()

    class Meta:
        db_table = 'sales_data'
        managed = False  # Since the table already exists

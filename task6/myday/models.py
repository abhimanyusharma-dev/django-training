from django.db import models

# Create your models here.
class product(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=30)
    p_price = models.FloatField()
    p_offer = models.FloatField()
    
    def __str__(self):
        return self.p_name

      
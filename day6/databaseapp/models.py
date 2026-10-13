from django.db import models

# Create your models here.
class client(models.Model):
    client_id = models.IntegerField()
    cname = models.CharField(max_length=100)
    c_company=models.CharField(max_length=40)


    def __str__(self):
        return self.cname



class customer(models.Model):
    customer_id = models.IntegerField()
    cus_name = models.CharField(max_length=100)
    cus_moblie=models.CharField(max_length=40)


    def __str__(self):
        return self.cus_name
      
      
      
class order(models.Model):
    order_id = models.IntegerField()
    order_no = models.IntegerField()
    order_price = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order_id}"
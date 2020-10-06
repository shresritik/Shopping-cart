from django.db import models


# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=500,default="")
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='images',default="")
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=500,default="")
    phone = models.CharField(max_length=20, default="")
    msg=models.CharField(max_length=500,default="")


    def __str__(self):
        return self.name
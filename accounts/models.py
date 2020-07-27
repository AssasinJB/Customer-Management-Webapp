from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250,null = True)
    phone = models.CharField(max_length=50,null = True)
    email = models.CharField(max_length=250,null = True)
    date_created = models.DateTimeField(auto_now_add=True,null = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=250,null = True)
    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (
        ('Outdoor','Outdoor'),
        ('Indoor','Indoor')
    )

    name =models.CharField(max_length=250,null = True)
    price = models.FloatField(null = True)
    description =models.CharField(max_length=250,null = True,blank = True)
    category =models.CharField(max_length=250,null = True,choices = CATEGORY)
    date_created =models.DateTimeField(auto_now_add=True,null = True)
    tag =models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('delivered','delivered'),
    )
    product =models.ForeignKey(Products,null = True,on_delete=models.SET_NULL)
    customer =models.ForeignKey(Customer,null = True,on_delete=models.SET_NULL)
    status = models.CharField(max_length = 200,null = True,choices = STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null = True)
    note = models.CharField(max_length=50,null = True)
    
    def __str__(self):
        return self.product.name
from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phno = models.CharField(max_length=200,null=True)
    create_at = models.CharField(max_length=200,null=True)

    def __str__(self):
        return  self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
        


class Product(models.Model):
    category=(
        ('indoor','In Door'),
        ('outdoor','Out Door')
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=category)
    description=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name   

class Order(models.Model):
    status = (
        ('pending' , 'Pending'),
        ('out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer =  models.ForeignKey(Customers,max_length=200,null=True,on_delete=SET_NULL)
    product=  models.ForeignKey(Product,max_length=200,null=True,on_delete=SET_NULL)
    created_at=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=status)

    def __str__(self):
        return self.product.name


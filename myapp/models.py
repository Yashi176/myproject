from email.policy import default
from django.db import models

# Create your models here
class Size(models.Model):
#     Size_id=models.IntegerField()
#     Size_code=models.CharField(max_length=50)
    Size_name=models.CharField(max_length=50)
class Colour(models.Model):
    # Colour_id=models.IntegerField()
    ColourName=models.CharField(max_length=50)
class BrandName(models.Model):
    Brand_name=models.CharField(max_length=50)
class ProductTable(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.FloatField()
    stock=models.IntegerField()
    size=models.ForeignKey("Size",on_delete=models.CASCADE)
    colours=models.ForeignKey("Colour",on_delete=models.CASCADE)
    Brand=models.ForeignKey("BrandName",on_delete=models.CASCADE)
    image=models.ImageField()
class User(models.Model):
    Email=models.EmailField()
    Name=models.CharField(max_length=50)
    Phone_no=models.IntegerField()
    Password=models.CharField(max_length=50)
    CreatedAt=models.DateTimeField()
class cart(models.Model):
    userid=models.ForeignKey("User",on_delete=models.CASCADE)
    p_name=models.CharField(max_length=50)
    qty=models.IntegerField()
    p_price=models.FloatField()
    t_price=models.FloatField()
    dlvry_add=models.TextField()  
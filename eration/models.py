from django.db import models

# Create your models here.

class Admin(models.Model):
      name=models.CharField(max_length=10,default="")
      password=models.CharField(max_length=10,default="")


class  User(models.Model):
    name=models.CharField(max_length=10,default="")
    cardnumber=models.CharField(max_length=10,default="")
    cardtype=models.CharField(max_length=10,default="")

class RegistrationDetail(models.Model):
    name=models.CharField(max_length=10,default="")
    adharnumber=models.CharField(max_length=10,default="")
    housenumber=models.CharField(max_length=10,default="")
    address=models.CharField(max_length=10,default="")
    village=models.CharField(max_length=10,default="")
    localtype=models.CharField(max_length=10,default="")
    taluk=models.CharField(max_length=10,default="")
    localname=models.CharField(max_length=10,default="")
    mobileno=models.CharField(max_length=10,default="")
    email=models.CharField(max_length=10,default="")
    cardnumber=models.CharField(max_length=10,default="")
    cardtype=models.CharField(max_length=10,default="")
    photo=models.FileField(upload_to='images',default='')
    password=models.CharField(max_length=10,default="")

    class Meta:
      db_table = "eration_registrationdetail"


class Feedback(models.Model):
    cardnumber=models.CharField(max_length=10,default="")
    feedback=models.CharField(max_length=10,default="")

    
class Notification(models.Model):
    cardnumber=models.CharField(max_length=10,default="")
    notification=models.CharField(max_length=10,default="")

class Product(models.Model):
    product_id=models.CharField(max_length=10,default="")
    productname=models.CharField(max_length=10,default="")
    quantity=models.CharField(max_length=10,default="")
    price=models.CharField(max_length=10,default="")

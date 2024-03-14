from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):   #this creates a 'User' table in the database
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name= models.CharField(max_length=255)
    age=models.PositiveBigIntegerField(null=True)


class Products(models.Model):   
    p_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    p_name= models.CharField(max_length=255)
    p_modelno=models.PositiveBigIntegerField(null=True)




# class Profile(models.Model):

#     profile_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

#     profile_pic=models.ImageField(blank=True,default='cat.jpeg')

#     profile_description=models.TextField(max_length=225,default='null')
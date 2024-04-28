from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
class Products(models.Model):
    title= models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.title
class User(models.Model):
    name= models.CharField(max_length=50,null=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

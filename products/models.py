from django.db import models
from datetime import datetime
class Product(models.Model):
    cate=[
        ('Phone','Phone'),
        ('Computer','Computer'),
    ]
    name= models.CharField(max_length=50,default='name')
    price= models.DecimalField(max_digits=6,decimal_places=2)
    content=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50,blank=True,null=True,choices=cate)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['price']
        
class Test(models.Model):
    date=models.DateField()
    time= models.TimeField(null=True)
    created =models.DateTimeField(default=datetime.now)
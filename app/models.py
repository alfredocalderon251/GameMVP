"""
Definition of models.
"""

from django.db import models
from django.conf import settings

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class tag(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    front_Image=models.URLField()
    categories=models.ManyToManyField(category)
    tags=models.ManyToManyField(tag)
    price=models.FloatField()
    GameDate=models.DateField()

    def __str__(self):
        return self.name

class gameplayimages(models.Model):
    Prod=models.ForeignKey(Product, on_delete=models.CASCADE)
    imageURL=models.URLField()

        

class youtubevideo(models.Model):
    Prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    videourl=models.URLField()

class cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class mygames(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    productkey=models.CharField(max_length=255)
    dateofpurchase=models.DateField()
        
        


#class Genre(models.Model):
#    name=models.CharField(max_length=255)

#    def __str__(self):
#        return self.name

#class Movie(models.Model):
#    title=models.CharField(max_length=255)
#    star =models.CharField(max_length=255)
#    release_year=models.IntegerField()
#    price=models.FloatField()
#    in_stock=models.IntegerField()
#    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
#    in_4k=models.BooleanField()
#    director=models.CharField(max_length=255)
#    image_url=models.TextField()
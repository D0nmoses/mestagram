from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=20)


class Category(models.Model):
    category = models.CharField(max_length=10)


class Image(models.Model):
    image = models.ImageField(upload_to='images', default='default-no-image-1.png')
    image_name = models.CharField(max_length=20)
    imade_description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ManyToManyField(Category)






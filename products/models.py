from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    #category_image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    package_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
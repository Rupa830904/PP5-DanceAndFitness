from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    category_image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

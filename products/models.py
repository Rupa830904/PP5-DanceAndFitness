from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    package_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
    
    def num_of_reviews(self):
        return self.review_set.count()

    def average_rating(self):
        from django.db.models import Avg
        # return Review.objects.filter('product=self').aggregate(Avg('rating'))['rating__avg']
        return Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
    

class Review(models.Model):
    product = models.ForeignKey('Package', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    #id = models.UUIDField(default=uuid.uuid4, max_length=36, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.user} review for {self.product}'
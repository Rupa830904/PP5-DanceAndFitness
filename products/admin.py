from django.contrib import admin

# Register your models here.

from .models import Package, Category

# Register your models here.

class PackageAdmin(admin.ModelAdmin):
     list_display = (
        'name',
        'category',
        'description',
        'price',
        'package_image',
    )

     ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Package, PackageAdmin)
admin.site.register(Category, CategoryAdmin)
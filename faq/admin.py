from django.contrib import admin

# Register your models here.

from .models import Contact, Subscribe

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'question',
        'answer',
        'subscribe',
    )


admin.site.register(Contact, ContactAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )


admin.site.register(Subscribe, SubscribeAdmin)

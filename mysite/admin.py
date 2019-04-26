from django.contrib import admin
from mysite import models

# Register your models here.
admin.site.register(models.Maker)
admin.site.register(models.PModel)

class ProductAdmin(admin.ModelAdmin):
    list_display=('pmodel', 'nickname', 'price', 'year')

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PPhoto)

from django.contrib import admin

from api.models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','image']

    def __str__(self):
        return self.name

admin.site.register(Shop, ShopAdmin)

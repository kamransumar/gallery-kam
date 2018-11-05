from django.contrib import admin
from .models import Location, categories, Picture

# Register your models here.


class PictureAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)


admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Picture, PictureAdmin)

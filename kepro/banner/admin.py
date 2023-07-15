from django.contrib import admin

# Register your models here.
from .models import BannerImg
class BannerImgAdmin(admin.ModelAdmin):
    list_display = ['title','image']
admin.site.register(BannerImg,BannerImgAdmin)



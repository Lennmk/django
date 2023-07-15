from django.db import models

# Create your models here.
class BannerImg(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"标题", default="")
    image = models.ImageField(upload_to="static/upload/banner/%Y/%m", verbose_name=u"图片", max_length=100)

    class Meta:#内部类
        verbose_name = "广告图"
        verbose_name_plural = verbose_name#模型类的复数名，如果不设置则是小写的模型名

    def __str__(self):
        return self.title


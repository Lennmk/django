from django.contrib import admin
from .models import CourseClass,Course,Lesson,Video
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(CourseClass)
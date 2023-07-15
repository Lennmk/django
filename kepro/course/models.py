from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
from organization.models import CourseOrg, Teacher


class CourseClass(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"分类名")

    class Meta:
        verbose_name = u"课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    courseclass = models.ForeignKey(CourseClass, on_delete=models.CASCADE, verbose_name=u"课程分类", null=True, blank=True)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # 被注释
    """
    detail =models.CharField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')"""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="static/upload/courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")

    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    get_zj_nums.short_description = "章节数"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

from django.shortcuts import render
from .models import CourseOrg,Teacher
from django.views.generic.base import View
# Crate your views here.
class OrgDescView(View):
    """机构介绍页面"""
    def get(self,request,org_id):
        #通过id查找数据
        course_org=CourseOrg.objects.get(id=int(org_id))
        #返回页面和这条数据
        return render(request,'org-detail-desc.html',{
            'course_org':course_org
        })

class OrgCourseView(View):
    """机构课程页面"""
    def get(self,request,org_id):
        # 通过id查找数据
        course_org=CourseOrg.objects.get(id=int(org_id))
        #通过父类查找子类的所有数据
        all_courses=course_org.course_set.all()
        #返回页面和数据
        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'course_org':course_org,
        })
class OrgTeacherView(View):
    """机构讲师页面"""
    def get(self,request,org_id):
        # 通过id查找数据
        course_org=CourseOrg.objects.get(id=int(org_id))
        # 通过父类查找子类的所有数据
        all_teachers=course_org.teacher_set.all()
        # 返回页面和数据
        return render(request,'org-detail-teachers.html',{
            'all_teachers':all_teachers,
            'course_org':course_org,
        })
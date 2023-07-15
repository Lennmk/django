from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from banner.models import BannerImg
from .models import Course
from django.views.generic.base import View
from django.db.models import Q   #多个查询使用Q
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

class IndexView(View):
    """主页页面"""
    def get(self,request):
        #登录验证
        if request.user.is_authenticated:
            #获取所有数据
            all_banners=BannerImg.objects.all()
            #查找每个学校课程的前十条内容
            itcourses=Course.objects.filter(courseclass=1)[:10]
            xqcourses = Course.objects.filter(courseclass=2)[:10]
            yycourses = Course.objects.filter(courseclass=3)[:10]
            #返回页面
            return render(request,'index.html',{
                'all_banners':all_banners,
                'itcourses':itcourses,
                'xqcourses':xqcourses,
                'yycourses':yycourses,
            })
        else:
            #没有登录就跳转登录页面
            return redirect(reverse('courses:login')+'?next='+request.path)
def outlogin(request):
    # 注销登录
    request.session.delete()
    return redirect(reverse('index'))
def loginView(request):
    #获取跳转的页面path
    redirect_path=request.GET.get('next','')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                # 如果验证通过
                if user.is_active:
                    login(request, user)
                    r = redirect(redirect_path)

                else:
                    #输出密码错误
                    msg = '用户密码错误'
                    r=HttpResponse(msg)
            else:
                msg = '用户名不存在'
                r=HttpResponse(msg)
            return r

        else:
            msg = '密码错误'
            return HttpResponse(msg)
    else:
        return render(request, 'login.html',{'next':redirect_path})

class CourseDetailView(View):
    """课程详细介绍"""
    def get(self,request,course_id):
        #登录验证
        if request.user.is_authenticated:
            #获取课程内容
            course=Course.objects.get(id=int(course_id))
            #点击数量加1
            course.click_nums+=1
            #保存
            course.save()
            #获取相关课程
            tag=course.tag
            #如果存在
            if tag:
                #查找出一条数据
                relate_coures=Course.objects.filter(Q(id=int(course_id)) & Q(tag=tag))[:1]
            else:
                #否则为空
                relate_coures=[]
            #返回数据和内容
            return render(request,'course-detail.html',{
                "course":course,
                "relate_coures":relate_coures,
            })
        else:
            return redirect(reverse('courses:login'))

class CourseInfoView(View):
    """章节信息"""
    #登录验证
    def get(self,request,course_id):
        if request.user.is_authenticated:
            #获取数据
            course=Course.objects.get(id=int(course_id))
            #学习人数+1
            course.students+=1
            #保存
            course.save()
            #返回数据和内容
            return render(request,'course-video.html',{
                "course":course
            })
        else:
            return redirect(reverse('courses:login'))

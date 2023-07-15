from django.urls import path,re_path
from .views import CourseInfoView
from .views import IndexView
from .views import CourseDetailView
from .views import loginView,outlogin
#应用命名空间
app_name='courses'
urlpatterns=[
    # path('index/',IndexView.as_view(),name='index'),
    # 登录页面
    path('login/',loginView,name='login'),
    # 注销登录
    path('outlogin/',outlogin),
    #课程详情页
    re_path(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name='course_detail'),
    #课程章节
    re_path(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name='course_info'),
]
from django.urls import path,re_path,include
from .views import OrgDescView,OrgTeacherView,OrgCourseView
#应用命名空间
app_name='org'
urlpatterns=[
    #机构课程页面
    re_path(r'^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name='org_course'),
    #机构介绍页面
    re_path(r'^desc/(?P<org_id>\d+)/$',OrgDescView.as_view(),name='org_desc'),
    #机构讲师页面
    re_path(r'^org_teacher/(?P<org_id>\d+)/$',OrgTeacherView.as_view(),name='org_teacher'),
]
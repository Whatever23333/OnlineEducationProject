"""NeuOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from NeuOnline.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView,ResetView, ModifyPwdView
from organization.views import OrgView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^login/$', LoginView.as_view(), name="login"),
    re_path('^register/$', RegisterView.as_view(), name="register"),

    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),
    re_path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    path("modify_pwd/", ModifyPwdView.as_view(), name="modify_pwd"),


    #课程机构首页
    path('org_list/', OrgView.as_view(), name= 'org_list'),

    #处理上传文件的处理函数
    re_path('media/(?P<path>.*)', serve, {"document_root" : MEDIA_ROOT}),
]

"""为应用程序users定义URl模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = (
    # 登录页面
    url('login/', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # 注销
    url('logout/', views.logout_view, name='logout'),
    # 注册
    url('register/', views.register, name='register')
)
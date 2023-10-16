'''为应用程序users定义URL模式'''

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # include默认登录页面
    path('', include('django.contrib.auth.urls')),
    # 注册页面.
    path('register/', views.register, name='register'),
]
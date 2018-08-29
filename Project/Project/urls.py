"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from api import views as apiView
from django.conf.urls import include
import xadmin

urlpatterns = [
    # 后台模板
    path('admin/', xadmin.site.urls),
    path('apiauth/', include('rest_framework.urls')),
    # 获取等级金额关系
    # 发布订单
    # 接单
    # 确认订单
    # 交付订单
    # 结单
    # 沟通
]

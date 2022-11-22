"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from user import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    #url - /user/1 -> 이걸 처리할 함수랑 연결작업을 한다 
    path("user/index", views.index),
    path("user/info", views.info), 
    path("user/info2/<username>/<phone>", views.info2),

    #user/add/4/5
    path("user/add/<x>/<y>", views.add),

    #user/sub?x=5&y=8  => 5-8=-3
    path("user/sub", views.sub),

    #user/dan1/4
    path("user/dan1/<dan>", views.gugudan1)

    #user/dan2?dan=4
    #sadari/w1/w2/h
]

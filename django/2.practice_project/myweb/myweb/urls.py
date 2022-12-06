"""myweb URL Configuration

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
from django.urls import path, include

# app단위의 urls를 연결해주어야 거꾸로 갔을때
# project단위의 urls -> app단위의 urls -> app단위의 views -> templates단위의 html파일과 app 단위의 views의 상호작용
# app 단위의 admin과 forms는 app단위의 models에 의존하고 이 모두는 연결되어있다.
# 중간에 연결보조는 project단위의 settings의 INSTALLED_APPS, TEMPLATES영역을 통해서 가능하다.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('photo.urls'))
]

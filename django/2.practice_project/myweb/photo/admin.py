from django.contrib import admin
from .models import Photo

# 먼저 models.py에 등록된 클래스를 가져와서 관리자페이지에도 반영시켜주는 것이다.
# Register your models here.
admin.site.register(Photo)
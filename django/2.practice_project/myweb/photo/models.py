# models는 데이터베이스에 저장될 데이터의 형태를 정의하고, 기능을 설정해주는 공간이다.
# models에 class를 설정 및 변경해주고나서는 python manage.py makemigrations
# 그 다음에는 python manage.py migrate를 꼭 해주어야 한다.
# 그래야 내가 생성한 models이 적용되어서 사용이 가능하다.
# models에 class를 정의해주고 위의 설정변경을 적용해준 후에는 admin.py로 간다.

from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
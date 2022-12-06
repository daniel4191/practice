from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # general한 파일들 (pdf, picture, doc등을 저장하려면 FileField를,
    # 이미지만은 ImageField로 하는게 맞다.)
    image = models.ImageField(upload_to='images')

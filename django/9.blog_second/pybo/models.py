from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    # related_name을 추가해 줌으로 인해서 같은 모델을 참조하고 있음을 해소할 수 있다.
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question')
    # 제목
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 폼에서 데이터 검사시 값이 비워져 있어도 괜찮다는 의미다.
    modify_date = models.DateTimeField(null=True, blank=True)
    # 좋아요
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_answer')
    # on_delete와 이하 내용은 쉽게말해서 ForeignKey로 맞물려 있는 내용이 삭제되면 이 필드 또한
    # 삭제 해준다는 내용이다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 폼에서 데이터 검사시 값이 비워져 있어도 괜찮다는 의미다.
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True,
                               on_delete=models.CASCADE)

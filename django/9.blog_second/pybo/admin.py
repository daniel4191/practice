from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


# 위에서 클래스를 등록해주면 반드시 여기에도 추가를 해줘야한다.
admin.site.register(Question, QuestionAdmin)

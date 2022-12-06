from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True) # 책 ID
    title = models.CharField(max_length=50) # 제목
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()
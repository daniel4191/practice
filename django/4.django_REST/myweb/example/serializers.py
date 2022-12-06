# serailizers는 파이썬의 모델 데이터를 JSON으로 변환해 주는 것이다.
from rest_framework import serializers
from .models import Book

'''
class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField(primary_key=True)
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    pages = serializers.IntegerField()
    price = serializers.IntegerField()
    published_date = serializers.DateField()
    description = serializers.TextField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.bid = validated_data.get('bid', instance.bid)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.category = validated_data.get('category',instance.category)
        instance.pages = validated_data.get('pages',instance.pages)
        instance.price = validated_data.get('price',instance.price)
        instance.published_date = validated_data.get('published_date',instance.published_date)
        instance.description = validated_data.get('description',instance.description)
        instance.save()

        return instance
'''

# 위의 코드를 이렇게 클래스로 만들어 줄 수 있다.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']
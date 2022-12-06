from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Max, Min
from .models import Book
# Create your views here.


def index(request):
    # -를 붙여주면 DESC 효과를 보게된다.
    books = Book.objects.all().order_by('-title')
    num_books = books.count()
    # app단위에서 소개된 models.py의 rating을 가져와서 평균값을 내준다.
    avg_rating = books.aggregate(Avg('rating'))  # rating__avg, rating__min

    # 마지막 딕셔너리 화 한 'books': books를 templates의 html에 books라는 데이터로 보내준다.
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_number_of_books': num_books,
        'average_rating': avg_rating
    })

# id를 구분해서 상세내역을 출력해야하기때문에 id를 추가로 입력해주기로 했다.


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    #  book = get_object_or_404(Book, pk=id) 이 한줄이 위의 4줄로 엮인 try, except를 대신한다
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestseller
    })

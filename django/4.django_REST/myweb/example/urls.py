from django.urls import path, include
from .views import BooksAPIMixins, HelloAPI, BookAPI, BooksAPI, bookAPI, booksAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, BookAPIGenerics

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI), # FBV
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
    path('generic/books/', BooksAPIGenerics.as_view()),
    path('generic/book/<int:bid>/', BookAPIGenerics.as_view())
]
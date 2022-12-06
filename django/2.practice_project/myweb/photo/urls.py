from django.urls import path
from . import views

# ''는 기본주소 뒤쪽으로 쓰는 주소가 없다는 이야기고 <int:pk>는 pk라는 데이터가 넘어와야하는데, pk자료는 반드시 숫자여야한다. 라는 의미고
# 데이터는 views의 함수로부터 가져온다는 의미
urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name = 'photo_detail'),
    path('photo/new/', views.photo_post, name = 'photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name = 'photo_edit')
]

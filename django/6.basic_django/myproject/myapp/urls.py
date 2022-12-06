from django.urls import path

from . import views

# 프로젝트 단위의 urls로부터 전달이 되어서 온 것이고 프로젝트 단위의 urls가 ''로 공백처리로 끝났다면
# 여기 app 단위의 urls에서는 ''로 하게되면 그냥 기본적으로 127.0.0.1:8000 로 접속
# create/는 127.0.0.1:8000/create/ 이런식으로 가게 된다.
# read/1는 127.0.0.1:8000/read/1/ 이런식!

urlpatterns = [
    # views단위에 '' 주소 뒤의 것을 위임해주기 위해서 ''주소 뒤에 ,를 하고 views.~~ 를 사용한다.
    path('', views.index),
    path('create/', views.create),
    # <>는 변동이 될 수 있는 요소에 대해서 이렇게 입력을 하고
    # <a:b>의 첫번째인자 a는 b의 타입을 적어주어야하고
    # b는 views 함수를 쓸때 request옆에 인자로 넣어준다.
    # 그냥 b만 적어주어도 된다.
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]

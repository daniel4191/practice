from django.urls import path
# 놀라운 사실이다. 이것을 쓰면 굳이 views.py에서 뭔가를 안만들어줘도 내장함수로써의 역할을 할 수 있다는 점이
# 그리고 굳이 auth_views로 as 해주는 이유는 추 후에 views를 가져와서 사용할때 충돌을 방지하기 위해서다.
from django.contrib.auth import views as auth_views

from . import views

app_name = 'common'

urlpatterns = [
    # login mapping
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
    ), name="login"),
    # logout mapping
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # signup mapping
    path('signup/', views.signup, name='signup'),
]

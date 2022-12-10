from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views

# namespace (네임스페이스)
app_name = 'pybo'

# since herecode line

"""
# views.py 파일 하나로 관리해줄때의 코드
# 여기서 name을 지정해주는 이유는 html에서 사용하기 위한 매핑으로 쓰기 위해서다.
# urls.py에서 설정해주는 매핑이 더욱 유의미한 이유는 url 패턴이 계속해서 변경될 경우
# urls.py로 부터 비롯된 매핑이 아니면 일일이 하드코딩을 해주어야하기 때문이다.
urlpatterns = [
    path('', views.index, name='index'),
    # templates에서 탬플릿 태그를 통해서 href로 전송되는 연결다리를 해줄 매핑이다.
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/',
         views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name='question_create'),
    # question_modify edit mapping
    path('question/modify/<int:question_id>/', views.question_modify,
         name="question_modify"),
    # question delete comming jQuery mapping
    path('question/delete/<int:question_id>/', views.question_delete,
         name="question_delete"),

    # answer edit mapping
    path('answer/modify/<int:answer_id>/',
         views.answer_modify, name="answer_modify"),

    # answer delete mapping
    path('answer/delete/<int:answer_id>/',
         views.answer_delete, name="answer_delete"),

    # question side add comment mapping
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),

    # question side edit comment mapping
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question,
         name='comment_modify_question'),

    # question side delete mapping
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),

    # answer side add comment mapping
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer,
         name='comment_create_answer'),

    # answer side edit comment mapping
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer,
         name='comment_modify_answer'),

    # answer side delete mapping
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer,
         name='comment_delete_answer'),
]

'''
# generic view로 전환하게 되면 urlpatterns도 모두 아래와 같이 변경해줘야한다.

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>/', views.DetailView.as_view())
]
'''
"""

# views.py 파일에 넣어서 사용해야하는 기능들을 views라는 폴더에 각각의 기능대로 py파일을 만들어서 분할해주고
# 새롭게 매핑해줄때

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify,
         name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete,
         name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify,
         name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete,
         name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/',
         comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/',
         comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer,
         name='comment_delete_answer'),

    # vote_views.py
    path('vote/question/<int:question_id>/',
         vote_views.vote_question, name='vote_question'),

]

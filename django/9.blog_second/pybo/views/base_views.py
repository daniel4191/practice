# basic management
# index, detail

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


# code line

def index(request):
    '''

    printing pybo list
    '''

    # factor
    page = request.GET.get('page', '1')  # page

    # lookup
    question_list = Question.objects.order_by('-create_date')

    # paging process
    # showing 10contents in each pages
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    # 여기서 지정된 'question_list'가 templates에 귀속된 폴더로 html을 작성할때 활용되는
    # 일종의 name값으로 사용된다.
    context = {
        'question_list': page_obj
    }
    # 1 가장 기초가 되는 방식
    # return HttpResponse('hello, welcome!')

    # 2 그 다음 기초인 render 방식
    return render(request, 'pybo/question_list.html', context)


"""
# 위의 index를 generic view로 전환했을때

class IndexView(generic.ListView):
    '''

    printing pybo list
    '''

    def get_queryset(self):
        return Qeustion.objects.order_by('-create_date')

"""


def detail(request, question_id):
    '''

    printing pybo contents
    '''

    # 조회의 방식에는 get과 filter가 있다.
    # get은 지정해준 값 오직 하나의 값만 출력해주지만 filter는 list 형태로 출력함을 기억하자.
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    # 이것도 templates의 html에서 탬플릿 태그로 쓰이는 용도 인것같다.
    context = {
        'question': question
    }
    return render(request, 'pybo/question_detail.html', context)


"""
# 위의 detail을 generic view로 전환했을때
class DetailView(generic.DetailView):
    '''

    printing pybo contents
    '''
    model = Question
"""

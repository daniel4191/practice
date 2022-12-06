from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# my code in here


'''
이 review def 함수는 아래의 ReviewView로 대체한다.
def review(request):
    if request.method == 'POST':
        # existing_model = Review.objects.get(pk=1)
        form = ReviewForm(request.POST)
        # entered_username = request.POST['username']

        # if entered_username == '' and len(entered_username) >= 100:
        #     return render(request, 'reviews/review.html', {
        #         'has_error': True
        #     })
        # print(entered_username)

        if form.is_valid():
            # 만약 models로 이 기능들을 이용한다면, 굳이 이것을 써줄 필요는 없다.
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating'])
            # review.save()
            # form.cleaned_data는 input값을 통해서 제출된 값에 대해서 딕셔너리 형태로 출력한다.
            # 즉, 저장도 가능하다.
            # print(form.cleaned_data)

            form.save()
            return HttpResponseRedirect('/thank-you')

    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        # 'has_error': False
        'form': form
    })

'''


class ReviewView(CreateView):
    # 인자가 CreateView일때 사용하는 정의사항
    # CreateView는 특이하게 따로 save()를 하기위한 저장을
    # 할 필요가 없다.
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    '''
    # 인자가 FormView일때 사용하는 정의사항
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    # 이게 있어야 양식을 제출후에 이동페이지로 에러없이 넘어가는 것이 가능하다.
    success_url = '/thank-you'

    # 위의 정의사항만 있으면 폼을 제출했을때 저장이 안되기 때문에 제출된 폼을 저장하기 위해서
    # 이게 필요하다
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    '''
    # 인자가 View일때 사용하는 정의사항들
    '''
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')

        return render(request, 'reviews/review.html', {
            'form': form
        })
        '''


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messege'] = 'this works'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    # class에서 받는 인수가 ListView일 경우에 사용하는 것들
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

    # class에서 받는 인수가 TemplateView일 경우에 사용하는 것들
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favortie_id = request.session.get('favorite_review')
        context['is_favorite'] = favortie_id == str(loaded_review.id)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)

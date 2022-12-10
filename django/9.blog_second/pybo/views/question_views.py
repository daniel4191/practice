# question management
# question_create, question_modify, question_delete

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

# code line


@login_required(login_url='common:login')
def question_create(request):
    """

    pybo question submit
    """

    # form = QuestionForm()
    # return render(request, 'pybo/question_form.html', {
    #     'form': form
    # })

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            # models.py에 클래스 안에 추가된 author를 의미한다.
            question.author = request.user  # apply added author element
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')

    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """

    edit pybo question
    """

    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, "you don't have right for edit")
        return redirect('pybo:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # temporary save edit date
            question.save()
            return redirect('pybo:detail', question_id=question.id)

    # 위에서 묻는 if문이 POST였기에 자동적으로 여기는 GET
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form
    }
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """

    delete pybo question
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "you don't have permission to delete")
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

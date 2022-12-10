# answer management
# answer_create, answer_modify, answer_delete

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer

# code line


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """

    pybo answer submit
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # models.py에 클래스 안에 추가된 author를 의미한다.
            answer.author = request.user  # apply added author element
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # return redirect('pybo:detail', question_id=question.id)
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id
            ))

    else:
        form = AnswerForm()

    context = {
        'question': question, 'form': form
    }
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """

    edit pybo answer
    """

    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "you don't have permission to modify answer")
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect('pybo:detail', question_id=answer.question.id)
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail',
                            question_id=answer.question.id), answer.id
            ))

    else:
        form = AnswerForm(instance=answer)
    context = {
        'answer': answer,
        'form': form,
    }
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """

    delete pybo answer
    """

    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "you don't have permission to delete")

    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)

# vote management

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Question

# code line


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """

    register pybo question recommendations
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, "you can't recommend own yourself")

    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

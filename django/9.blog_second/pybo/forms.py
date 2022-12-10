from django import forms

from pybo.models import Question, Answer, Comment

# code area


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets영역은 css적용을 위해서 기입해주는 공간이다.
        # form.as_p같은 경우는 css를 이렇게 해야 먹일 수 있다.
        # widgets = {
        #     # attr은 atribute의 약어다
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        # }

        # labels는 내부적 엘레멘트를 쓸때 반드시 영어로 기입해야한다는 점 때문에, 사용자가 기입을 할때에
        # 한글등, 다른 언어로 해당 엘레멘트를 표현해줄 수 있는 영역이다.
        labels = {
            'subject': 'Title'
        }


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'contents'
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'contents',
        }

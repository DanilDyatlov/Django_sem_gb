from datetime import date

from django import forms

from .models import Author, Article, Comment


class AuthorForm(forms.ModelForm):
    birthday = forms.DateField(initial=date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'type': 'date'}))

    class Meta:
        model = Author
        fields = [
            'firstname',
            'lastname',
            'email',
            'biography',
        ]


class ArticleForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    cat_choices = [(f'Категория_{a}', f'Категория_{a}') for a in range(1, 21)]
    category = forms.ChoiceField(choices=cat_choices)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'views',
            'is_published',
        ]


class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=1, max_length=256, label='',
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Новый комментарий..'}))

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
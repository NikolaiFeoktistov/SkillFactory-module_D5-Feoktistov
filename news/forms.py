from django import forms
from .models import News

class NewsSearchForm(forms.Form):
    search_date = forms.DateField(required=False, label='Дата (ГГГГ-ММ-ДД)')
    search_title = forms.CharField(required=False, max_length=200, label='Название')
    search_author = forms.CharField(required=False, max_length=100, label='Автор')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']  # Здесь укажите поля, которые вы хотите редактировать

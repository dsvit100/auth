from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content') = 아래와 동일
        exclude = ('user', )
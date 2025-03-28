from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content') = 아래와 동일
        exclude = ('user', )


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # 보여줄 필드를 설정
        fields = ('content', )
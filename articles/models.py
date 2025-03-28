from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # 누구와 연결할 것인지(첫번째인자)


    # 1. 직접참조
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1은 추천하지 않음, 모델이 바뀔 수 있으므로(User)
    # 2. settings.py 활용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 3. get_user_model 함수 활용
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class comments(models.Model):
    content = models.TextField()
    # 두가지 요소와 1:N 관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 장고에서 제공하는 user 틀을 가져옴, 받아올 값을 추가하려면 아래에 추가할 수 있음
    pass
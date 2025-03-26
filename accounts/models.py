from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 장고에서 제공하는 user 틀을 가져옴, 받아올 값을 추가하려면 아래에 추가할 수 있음
    # 컬럼이 추가되면 정보 모두 삭제 후 User모델링부터 다시 해야하기 때문에, 미리 확장을 해 둔 것것
    pass
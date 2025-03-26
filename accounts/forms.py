from .models import User
from django.contrib.auth.forms import UserCreationForm

# 우리가 만든 폼으로 사용할거야

class CustomUserCreationForm(UserCreationForm):
    # model = AbstractUser 우리 user에 이미 이걸 상속받아왔는데 우리가 만들 폼과 뭐가 다르다는 말?
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('username', ) # 튜플로 적어야함. password는 필수여서 적지 않아도 출력됨
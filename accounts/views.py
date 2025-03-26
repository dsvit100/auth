from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# login이라는 함수를 우리가 만들었기 때문에, auth_login으로 이름을 바꿔줌

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        # 우리가 생성하려는 건 id/pw가 아니라 세션정보를 생성하는 것이기 때문에 request를 한 번 더 작성
        if form.is_valid():
            auth_login(request, form.get_user()) # id/pw에 맞는 값을 찾아주는 함수 (form.get_user), 값에 맞는 사용자에게 맞는 페이지를 제공해주기 위한
            #### 설명해주신대영
            return redirect('articles:index')

    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)
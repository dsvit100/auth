from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# login이라는 함수를 우리가 만들었기 때문에, auth_login으로 이름을 바꿔줌
from django.contrib.auth import logout as auth_logout
# 동일하게 auth_logout으로 바꿔줌

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
            next_url = request.GET.get('next') # ?뒤에 있는 값이 get으로 들어옴

            # next가 없을 때 => None or 'articles:index'
            # next가 있을 때 => 'articles/create' of 'articles/index'

            return redirect(next_url or 'articles:index')
            # next_url이 T이기 때문에 뒤는 무조건 T = 단축평가
            # articles/create로 접근했는데 login창이 나왔다면 -> 로그인 후 create로 들어감
            # login 단추를 통해 접근했다면 -> index로 들어감

    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)

def logout(request):
    # delete 로직
    auth_logout(request)
    # DB에 있는 세션 키값을 찾아서 지워줌
    return redirect('accounts:login')
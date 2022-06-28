from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .views import *
from .forms import *
from order.urls import *

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def user_signup(request):
    if request.user.is_authenticated:
        return redirect('order:order_list')

    if request.method == "POST":
        form = SignupForm(request.POST)

        # error handling
        error = {}

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            request.POST['is_agree']
        except:
            error['is_agree'] = "약관에 동의하셔야 합니다."

        try:
            validate_email(email)
        except ValidationError:
            error['email'] = '올바른 이메일 형식이 아닙니다.'
        else: 
            if Participant.objects.filter(email=email).exists():
                error['email'] = '이미 존재하는 이메일 입니다.'    

        try:
            validate_password(password1)
            validate_password(password2)
        except:
            error['password'] = "영문자, 숫자, 특수문자의 조합을 사용하세요."
        else:
            if password1 != password2:
                error['password'] = "입력하신 비밀번호가 서로 다릅니다."

        if Participant.objects.filter(username=username).exists():
            error['username'] = "이미 존재하는 아이디 입니다."

        # signup
        if len(error) != 0 or not(form.is_valid()):
            context = {
                'form' : form
            }
            context.update(error)
            return render(request, 'user/user_signup.html', context)
        else:
            form.save()
            return redirect('user:user_signup_success')
    
    else:
        form = SignupForm()
        context = {
            'form' : form,
        }
        return render(request, 'user/user_signup.html', context)

@csrf_protect
def user_login(request):
    if request.user.is_authenticated:
        return redirect('order:order_list')

    if request.method == "POST":
        form = LoginForm(request.POST)
        
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('order:order_list')
        else:
            context = {
                'form': form,
                'error': "아이디 혹은 비밀번호를 다시 확인해주세요",
            }
            return render(request, 'user/user_login.html', context)

    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_login.html', context)

@csrf_protect
def user_logout(request):
    if request.method == "POST" and request.user.is_authenticated:
        logout(request)

    return redirect('order:order_list')
                

def user_signup_success(request):
    if request.user.is_authenticated:
        return redirect("order:order_list")
    else:
        context = {

        }
        return render(request, 'user/user_signup_success.html', context)

from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib.auth import login

from user.forms import LoginForm
from user.models import Participant
from order.models import Order
from .models import *;

"""
사실상 My Page의 역할
"""
def funding_list(request):
    if request.user.is_authenticated:
        try:
            status = request.GET['status']
        except:
            status = '0'

        # 0 -> 전체, 1 -> 만료 이전, 2 -> 만료
        if status == '1':
            fundings = Fund.objects.filter(order__order_status=False, participant=request.user)
        elif status == '2':
            fundings = Fund.objects.filter(order__order_status=True, participant=request.user)
        else:
            fundings = Fund.objects.filter(participant=request.user)

        fundings = list(fundings)
        fundings.sort(key=lambda x: x.order.target_time, reverse=True)

        context = {
            'user': request.user,
            'fundings': fundings,
            'status': status,
        }
        return render(request, "funding/funding_list.html", context)

    else :
        return redirect('funding:funding_login')

@csrf_protect
def funding_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('funding:funding_list')
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


"""
pk : order.pk
"""
#TODO : Front 에서 확인 후 Handling -> 만약 만료된 주문을 신청하려 하는 경우
def funding_create(request, pk):
    if request.method == "POST":
        order = get_object_or_404(Order, pk=pk)
        Fund.objects.create(
            order=order,
            participant=request.user,
        )
    return redirect("order:order_read", pk)

"""
pk : funding.pk
"""
def funding_delete(request, pk):
    fund = get_object_or_404(Fund, pk=pk)
    if request.method == "POST":
        fund = get_object_or_404(Fund, pk=pk)
        if fund.participant == request.user:
            fund.delete()
    return redirect("order:order_read", fund.order.pk)
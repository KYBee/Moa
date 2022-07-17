from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .models import *
from funding.models import *
from .forms import *
from django.core.paginator import Paginator

def order_list(request):
    try:
        sort = request.GET["sort"]
        status = request.GET["status"]
        # page = request.GET['page']
    except:
        sort = '0'
        status = '0'
        # page = '1'

    # Query String을 통한 정렬
    if sort == '1':
        orders = Order.objects.all().order_by('target_time')
    else:
        orders = Order.objects.all().order_by('-created_at')

    # Query String을 통한 미완료, 전체 주문 Filtering
    if status == '1':
        orders = orders.filter(order_status=False)

    #Pagination Code
    # paginator = Paginator(orders, PAGINATOR_COUNT)

    # if page == None:
    #     page = 1
    
    # orders = paginator.get_page(page)

    context = {
        'orders': orders,
        'sort' : sort,
        'status' : status,
        # 'page': page,
    } 

    return render(request, 'order/order_list.html', context)

def order_read(request, pk):
    order = get_object_or_404(Order, pk=pk)
    fund = None
    if request.user.is_authenticated:
        if Fund.objects.filter(participant=request.user, order=order).exists():
            fund = get_object_or_404(Fund, participant=request.user, order=order)

    context = {
        'order': order,
        'fund' : fund
    }

    return render(request, 'order/order_read.html', context)

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            # open chat url validation
            try:
                order = form.save(commit=False)

                validate = URLValidator()
                validate(order.chat_room)

                order.host = request.user
                order.save()

                Fund.objects.create(
                    order=order,
                    participant=request.user,
                )
                return redirect('order:order_read', order.pk)
            except:
                pass
            
        context = {
            'form': form,
        }
        return render(request, 'order/order_create.html', context)

    else:
        form = OrderForm()
        context = {
            'form' : form,
        }
        return render(request, 'order/order_create.html', context)


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order:order_read', order.pk)
        else:
            return redirect('order:order_list')
    else:
        form = OrderForm(instance=order)
        context = {
            'form': form
        }
        return render(request, 'order/order_update.html', context)


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect('order:order_list')
    else:
        redirect('order:order_read', order.pk)

def order_close(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST" and request.user == order.host:

        order.order_status = True
        order.save()

        return redirect('order:order_read', order.pk)
    else:
        redirect('order:order_read', order.pk)

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from funding.models import *
from .forms import *
from django.core.paginator import Paginator

def order_list(request):
    orders = Order.objects.all()

    #Pagination Code
    context = {
        'orders': orders
    } 

    return render(request, 'order/order_list.html', context)

def order_read(request, pk):
    order = get_object_or_404(Order, pk=pk)
    fund = None
    if Fund.objects.filter(participant=request.user, order=order).exists():
        fund = get_object_or_404(Fund, participant=request.user, order=order)

    context = {
        'order': order,
        'fund' : fund
    }
    print(context)

    return render(request, 'order/order_read.html', context)

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.host = request.user
            order.save()

            return redirect('order:order_read', order.pk)

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
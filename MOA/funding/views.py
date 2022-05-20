from django.shortcuts import render, redirect, get_object_or_404
from user.models import Participant
from order.models import Order
from .models import *;

"""
pk : user.pk
"""
def funding_list(request):
    fundings = Fund.objects.filter(participant=request.user)
    context = {
        'fundings': fundings
    }
    return render(request, "funding/funding_list.html", context)

"""
pk : order.pk
"""
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
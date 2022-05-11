from django.db import models
from order.models import Order
from user.models import Participant

# Create your models here.
class Fund(models.Model):
    fund_id = models.PositiveIntegerField()
    is_complete = models.BooleanField(default=False, verbose_name="완료여부")
    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now_add=True, verbose_name="수정일")
    order_id = models.ForeinKey(Order, on_delete=models.SET_NULL, related_name="order_set")
    participant_id = models.ForeinKey(Participant, on_delete=models.SET_NULL, related_name="participant_set")
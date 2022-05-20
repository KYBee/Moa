from django.db import models
from django.db.models import F, Q
from user.models import Participant

class Order(models.Model):
    store = models.CharField(max_length=30, verbose_name="상호")
    receive_place = models.CharField(max_length=30, verbose_name="배송 희망 위치")
    host = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="host_set", verbose_name="펀딩개설자", blank=True, null=True)
    order_status = models.BooleanField(default=False, verbose_name="펀딩상태")
    target_people = models.PositiveIntegerField(verbose_name="펀딩 희망 인원")
    target_money = models.PositiveIntegerField(verbose_name="펀딩 필요 금액")
    target_time = models.DateTimeField(verbose_name="완료시간")
    chat_room = models.URLField(max_length=200, null=True, blank=True, verbose_name="오픈채팅방 링크")
    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now_add=True, verbose_name="수정일")

    def __str__(self):
        return "{0} {1}".format(self.store, self.host)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(target_time__gt=F('updated_at')),
                name = "target_time_earlier_than_now"
            )
        ]
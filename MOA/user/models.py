from django.db import models
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, verbose_name="닉네임")
    email = models.EmailField(unique=True, verbose_name="이메일")
    is_agree = models.BooleanField(default=False, verbose_name="약관동의")
    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now_add=True, verbose_name="수정일")
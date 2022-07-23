from django.contrib import admin
from .models import *


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
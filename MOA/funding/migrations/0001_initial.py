# Generated by Django 3.2 on 2022-05-11 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False, verbose_name='완료여부')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='수정일')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_set', to='order.order')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
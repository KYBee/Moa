# Generated by Django 3.2 on 2022-07-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_chat_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='target_money',
            field=models.CharField(default='무관', max_length=5, verbose_name='펀딩 필요 금액'),
        ),
        migrations.AlterField(
            model_name='order',
            name='target_people',
            field=models.CharField(default='무관', max_length=5, verbose_name='펀딩 희망 인원'),
        ),
    ]

# Generated by Django 3.2 on 2022-07-17 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220717_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='target_money',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='펀딩 필요 금액'),
        ),
        migrations.AlterField(
            model_name='order',
            name='target_people',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='펀딩 희망 인원'),
        ),
    ]

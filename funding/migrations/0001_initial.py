# Generated by Django 3.2 on 2022-05-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False, verbose_name='완료여부')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='수정일')),
            ],
        ),
    ]

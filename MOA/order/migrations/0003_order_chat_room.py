# Generated by Django 3.2 on 2022-05-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='chat_room',
            field=models.URLField(blank=True, null=True, verbose_name='오픈채팅방 링크'),
        ),
    ]

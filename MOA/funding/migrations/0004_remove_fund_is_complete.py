# Generated by Django 3.2 on 2022-07-23 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_fund_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='is_complete',
        ),
    ]

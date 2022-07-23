# Generated by Django 3.2 on 2022-05-20 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_set', to=settings.AUTH_USER_MODEL, verbose_name='펀딩개설자'),
        ),
        migrations.AddConstraint(
            model_name='order',
            constraint=models.CheckConstraint(check=models.Q(target_time__gt=django.db.models.expressions.F('updated_at')), name='target_time_earlier_than_now'),
        ),
    ]

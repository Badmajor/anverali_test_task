# Generated by Django 5.0.4 on 2024-04-23 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_orders_customuser_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='orders',
        ),
        migrations.AddField(
            model_name='order',
            name='contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
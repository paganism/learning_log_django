# Generated by Django 2.2 on 2019-05-02 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20190502_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]

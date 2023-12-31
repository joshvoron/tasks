# Generated by Django 4.2.5 on 2023-10-13 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0002_alter_colormodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colormodel',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_colors', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='user_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_user_color', to='taskmanager.colormodel', to_field='user_color'),
        ),
    ]

from django.db import models
from authmodule.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django import forms
from django.db import IntegrityError
from django.db import models
from authmodule.models import CustomUser

class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    user_color = models.ForeignKey(to='ColorModel', to_field='user_color', on_delete=models.CASCADE, related_name='task_user_color')
    description = models.TextField(null=True, blank=True)
    expiration_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(to=CustomUser, to_field='username', on_delete=models.CASCADE, related_name='task_username', blank=False, null=False)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class ColorModel(models.Model):
    name = models.CharField(max_length=50)

    class Colors(models.IntegerChoices):
        RED = 1
        GREEN = 2
        BLUE = 3
        YELLOW = 4
        ORANGE = 5

    color = models.IntegerField(choices=Colors.choices)
    username = models.ForeignKey(to=CustomUser, to_field='username', on_delete=models.CASCADE, related_name='user_colors', blank=False, null=False)
    user_color = models.CharField(max_length=100, unique=True, default='1')



    def __str__(self):
        return self.user_color

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'

@receiver(pre_save, sender=ColorModel)
def set_user_color(sender, instance, **kwargs):
    try:
        instance.user_color = f"{instance.username.id} - {instance.color}"
    except IntegrityError as e:
        instance.error_message = 'This color already exists.'




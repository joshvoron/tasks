from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    color = models.ForeignKey(to='ColorModel',to_field='color', on_delete=models.PROTECT, related_name='tasks')
    description = models.TextField()
    expiration_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)

class ColorModel(models.Model):
    name = models.CharField(max_length=50)
    class Colors(models.IntegerChoices):
        RED = 1,
        GREEN = 2,
        BLUE = 3,
        YELLOW = 4,
        ORANGE = 5,
    color = models.IntegerField(choices=Colors.choices, unique=True, default=Colors.RED)

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
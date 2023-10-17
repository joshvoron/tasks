from django.forms import ModelForm
from .models import TaskModel, ColorModel

class TaskCreateForm(ModelForm):
    class Meta:
        model=TaskModel
        fields = ('title','user_color','description','expiration_date')

class TaskUpdateForm(ModelForm):
    class Meta:
        model=TaskModel
        fields = ('title','user_color','description','expiration_date')

class ColorCreateForm(ModelForm):
    class Meta:
        model = ColorModel
        fields = ('name', 'color')

class ColorUpdateForm(ModelForm):
    class Meta:
        model = ColorModel
        fields = ('name',)

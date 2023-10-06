from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from taskmanager.models import TaskModel, ColorModel
from taskmanager.forms import TaskCreateForm, TaskUpdateForm, ColorCreateForm
from django.utils import timezone


# Create your views here.
def index(request):
    tasks = TaskModel.objects.order_by('-expiration_date')
    colors = ColorModel.objects.all()
    count = len(colors)
    context = {
        'colorscount' : count,
        'tasks': tasks,
        'colors': colors,
    }
    return render(request,'index.html', context)

def by_color(request, color):
    tasks = TaskModel.objects.filter(color = color)
    colors = ColorModel.objects.all()
    count = len(colors)
    context = {
        'tasks' : tasks,
        'colors' : colors,
        'colorscount': count,
    }
    return render(request,'index.html', context)

class ColorCreateView(CreateView):
    template_name = 'colorcreate.html'
    form_class = ColorCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = ColorModel.objects.all()
        return context

class TaskCreateView(CreateView):
    template_name = 'taskcreate.html'
    form_class = TaskCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = TaskModel.objects.order_by('expiration_date')
        context['colors'] = ColorModel.objects.all()
        return context


class TaskDeleteView(DeleteView):
    template_name = 'taskdelete.html'
    model = TaskModel
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class TaskUpdateView(UpdateView):
    template_name = 'taskedit.html'
    form_class = TaskUpdateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs['pk']
        task = get_object_or_404(TaskModel, pk=task_id)

        context['task'] = task
        context['formatted_expiration_date'] = task.expiration_date.strftime("%Y-%m-%dT%H:%M")
        context['colors'] = ColorModel.objects.all()
        return context

    def get_object(self, queryset=None):
        task_id = self.kwargs['pk']
        return get_object_or_404(TaskModel, pk=task_id)

    def get_queryset(self):
        return TaskModel.objects.order_by('id')


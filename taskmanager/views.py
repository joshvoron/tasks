from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from taskmanager.models import TaskModel, ColorModel
from taskmanager.forms import TaskCreateForm, TaskUpdateForm, ColorCreateForm, ColorUpdateForm
from django.urls import reverse
from django.db import IntegrityError

# Create your views here.
# def index(request, self):
#     tasks = TaskModel.objects.filter(username=self.kwargs['username'])
#     colors = ColorModel.objects.all()
#     count = len(colors)
#     context = {
#         'colorscount' : count,
#         'tasks': tasks,
#         'colors': colors,
#     }
#     return render(request,'index.html', context)

def task_done(request, pk):
    task = TaskModel.objects.get(pk=pk)
    if task.username == request.user:
        task.done = True
        task.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

class TaskListView(ListView):
    template_name = 'index.html'
    queryset = TaskModel.objects.all()
    ordering = ('-creation_date')

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        return queryset.filter(username=self.request.user.username)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data()
        context['tasks'] = TaskModel.objects.filter(username=self.request.user.username, done=False)
        context['donetasks'] = TaskModel.objects.filter(username=self.request.user.username, done=True)
        context['colors'] = ColorModel.objects.filter(username=self.request.user.username)
        context['colorscount'] = len(ColorModel.objects.filter(username=self.request.user.username))
        return context



def by_color(request, user_color):
    color = ColorModel.objects.get(user_color=user_color).user_color
    tasks = TaskModel.objects.filter(user_color=color, username=request.user.username, done=False)
    donetasks = TaskModel.objects.filter(user_color=color, username=request.user.username, done=True)
    colors = ColorModel.objects.filter(username=request.user.username)
    count = len(colors)
    context = {
        'tasks': tasks,
        'colors': colors,
        'colorscount': count,
        'donetasks' : donetasks,
    }
    return render(request, 'index.html', context)


class ColorCreateView(CreateView):
    template_name = 'colorcreate.html'
    form_class = ColorCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = ColorModel.objects.filter(username=self.request.user.username)
        context['colorscount'] = len(ColorModel.objects.filter(username=self.request.user.username))
        return context

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.username = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('color', 'This color already exists.')
            return super().form_invalid(form)


class TaskCreateView(CreateView):
    template_name = 'taskcreate.html'
    form_class = TaskCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = TaskModel.objects.filter(username=self.request.user.username).order_by('expiration_date')
        context['colors'] = ColorModel.objects.filter(username=self.request.user.username)
        context['colorscount'] = len(ColorModel.objects.filter(username=self.request.user.username))
        return context

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    template_name = 'taskdelete.html'
    model = TaskModel
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colorscount'] = len(ColorModel.objects.all())
        context['User'] = self.request.user
        return context


class ColorUpdateView(UpdateView):
    template_name = 'coloredit.html'
    form_class = ColorUpdateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        color_id = self.kwargs['pk']
        color = get_object_or_404(ColorModel, pk=color_id)
        context['User'] = self.request.user
        context['color'] = color
        return context

    def get_object(self, queryset=None):
        color_id = self.kwargs['pk']
        return get_object_or_404(ColorModel, pk=color_id)

    def get_queryset(self):
        return ColorModel.objects.order_by('id')

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
        context['colors'] = ColorModel.objects.filter(username=self.request.user.username)
        context['colorscount'] = len(ColorModel.objects.all())
        context['User'] = self.request.user
        return context

    def get_object(self, queryset=None):
        task_id = self.kwargs['pk']
        return get_object_or_404(TaskModel, pk=task_id)

    def get_queryset(self):
        return TaskModel.objects.order_by('id')

class ColorDeleteView(DeleteView):
    template_name = 'colordelete.html'
    model = ColorModel
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colorscount'] = len(ColorModel.objects.all())
        context['User'] = self.request.user
        return context
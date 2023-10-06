from django.contrib import admin
from django.urls import path
from taskmanager.views import by_color, index, TaskCreateView, TaskUpdateView, TaskDeleteView, ColorCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create', TaskCreateView.as_view(), name='create'),
    path('edit/<int:pk>', TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('addcolor', ColorCreateView.as_view(), name='addcolor'),
    path('color/<int:color>',by_color, name = 'by_color')
]

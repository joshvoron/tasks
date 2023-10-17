from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from taskmanager.views import (by_color, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, ColorCreateView, ColorUpdateView, ColorDeleteView,
                               task_done)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='index'),
    path('create', login_required(TaskCreateView.as_view()), name='create'),
    path('edit/<int:pk>', login_required(TaskUpdateView.as_view()), name='edit'),
    path('coloredit/<int:pk>', login_required(ColorUpdateView.as_view()), name='coloredit'),
    path('delete/<int:pk>', login_required(TaskDeleteView.as_view()), name='delete'),
    path('colordelete/<int:pk>', login_required(ColorDeleteView.as_view()), name='color_delete'),
    path('done/<int:pk>', login_required(task_done), name='task_done'),
    path('addcolor', login_required(ColorCreateView.as_view()), name='addcolor'),
    path('color/<str:user_color>',login_required(by_color), name = 'by_color'),
    path('p/', include('authmodule.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
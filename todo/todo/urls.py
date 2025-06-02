from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),   # API endpoints prefix with /api/
]

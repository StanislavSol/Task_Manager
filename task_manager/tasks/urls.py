from django.urls import path
from task_manager.statuses import views


urlpatterns = [
     path('', views.ListTask.as_view(), name='tasks'),
     path('create/', views.CreateTask.as_view(), name='create_task'),
     path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
     path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
     path('<int:pk>/', view.Task.as_view(), name='task')
    ]

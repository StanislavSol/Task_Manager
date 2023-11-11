from django.urls import path
from task_manager.users import views

urlpatterns = [
     path('', views.IndexView.as_view(), name='users_index'),
     path('create/', views.CreateUserView.as_view(), name='create_users'),
     path('<int:id>/update/', views.EditUserView.as_view(), name='users_update'),
     path('<int:id>/delete/', views.UserFormDeleteView.as_view(), name='users_delete')
]

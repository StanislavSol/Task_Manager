from django.urls import path
from task_manager.users import views


urlpatterns = [
     path('', views.IndexView.as_view(), name='users_index'),
     path('create/', views.CreateUserView.as_view(), name='users_create'),
     path('<int:id>/update/', views.EditUserView.as_view(), name='users_update'),
     path('<int:id>/delete/', views.DeleteUserView.as_view(), name='users_delete'),
     path('login/', views.LoginUserView.as_view(), name='users_login'),
     path('logout/', views.logout_user, name='users_logout'),
]

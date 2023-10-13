from django.urls import path
from . import views

urlpatterns = [

#homepage
path('',views.home,name=""),

#register
path('register',views.register,name="register"),

#login
path('my-login',views.my_login,name="my-login"),

#dashboard
path('dashboard',views.dashboard,name="dashboard"),

#create a task
path('create-task',views.createTask,name="create-task"),

#read a task
path('view-tasks',views.viewTask,name="view-tasks"),

#update a task
path('update-task/<str:pk>/',views.updateTask,name="update-task"),

#delete a task
path('delete-task/<str:pk>/',views.deleteTask,name="delete-task"),

#logout
path('user-logout',views.user_logout,name="user-logout"),


]
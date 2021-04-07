from django.urls import path
from main.views import Index

urlpatterns = [
    path('', Index.index, name="index"),
    path('/goal/<int:pk>/update', Index.update_goal, name="update_goal"),
    path('/goal/<int:pk>/delete', Index.delete_goal, name="delete_goal"),
]

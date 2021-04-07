from django.urls import path
from main.views import Index
from main.views.auth import AuthView


urlpatterns = [
    path('', Index.index, name="index"),
    path('login/', AuthView.login, name="login"),
    path('logout/', AuthView.logout, name="logout"),
    path('change-password/', AuthView.change_password, name='change_password'),
    path('/goal/<int:pk>/update', Index.update_goal, name="update_goal"),
    path('/goal/<int:pk>/delete', Index.delete_goal, name="delete_goal"),
]

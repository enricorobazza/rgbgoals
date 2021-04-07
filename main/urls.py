from django.urls import path, include
from main.views import IndexView
from main.views.goals import GoalView
from main.views.auth import AuthView


urlpatterns = [
    path('', IndexView.index, name="index"),
    path('login/', AuthView.login, name="login"),
    path('logout/', AuthView.logout, name="logout"),
    path('change-password/', AuthView.change_password, name='change_password'),
    path('goal/', include([
        path('<int:pk>/', GoalView.list_one, name="list_one_goal"),
        path('<int:pk>/update/', GoalView.update, name="update_goal"),
        path('<int:pk>/delete/', GoalView.delete, name="delete_goal"),
    ]))
]

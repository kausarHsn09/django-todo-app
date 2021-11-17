
from .views import home_view,delete_todo
from django.urls import path

urlpatterns = [
    path('', home_view,name='home'),
    path('delete_todo/<todo_id>',delete_todo, name='deleteTodo')
]

# todo_list/todo_app/admin.py

from django.contrib import admin
from .models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)

from django.urls import path

from tasks.views import (
    CreateTaskView,
    TaskListView,
)


urlpatterns = [
    path("create/", CreateTaskView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
]

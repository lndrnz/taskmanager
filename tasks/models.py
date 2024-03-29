from django.db import models
from django.conf import settings
from projects.models import Project

USER_MODEL = settings.AUTH_USER_MODEL


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )
    assignee = models.ForeignKey(
        USER_MODEL, null=True, related_name="tasks", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    TASK_STATUS = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TASK_STATUS)
    assignee = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

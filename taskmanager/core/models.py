from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user
class User(AbstractUser):
    ROLE_CHOICES = [('Admin', 'Admin'), ('Manager', 'Manager'), ('Employee', 'Employee')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_deleted = models.BooleanField(default=False)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projects_created')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Task(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')]
    PRIORITY_CHOICES = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks_created')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Comment(models.Model):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Notification(models.Model):
    NOTIF_TYPE_CHOICES = [
        ('task_assigned', 'Task Assigned'),
        ('task_updated', 'Task Updated'),
        ('comment_added', 'Comment Added'),
    ]
    type = models.CharField(max_length=50, choices=NOTIF_TYPE_CHOICES)
    message = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    related_task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    related_comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

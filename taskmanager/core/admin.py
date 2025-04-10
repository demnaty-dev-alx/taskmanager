from django.contrib import admin
from core.models import (
    User, Project, Task,
    Notification, Comment
)

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Notification)
admin.site.register(Comment)

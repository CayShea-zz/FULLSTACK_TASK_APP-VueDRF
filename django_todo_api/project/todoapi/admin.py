from django.contrib import admin

from .models import User
from .models import Task

admin.site.register(User)
admin.site.register(Task)
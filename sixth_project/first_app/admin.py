from django.contrib import admin
from . import models
from first_app.models import StudentModel
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.StudentModel)
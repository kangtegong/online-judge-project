from django.contrib import admin
from .models import Course, Assignment, CodeSubmit, FileSubmit

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(CodeSubmit)
admin.site.register(FileSubmit)

from django.contrib import admin
from .models import Course, Module, ModuleContent

# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(ModuleContent)
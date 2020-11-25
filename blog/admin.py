from django.contrib import admin
from .models import Blog, subscribe, BlogComment#,techspresso, iros2020, research, 

# Register your models here.
# admin.site.register(techspresso)
"""admin.site.register(iros2020)
admin.site.register(research)"""
admin.site.register(subscribe)
admin.site.register(BlogComment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinymce.js',)

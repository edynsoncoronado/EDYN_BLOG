from django.contrib import admin
from .models import Category, Blog, Cover

admin.site.register(Category)
admin.site.register(Cover)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'active', 'created', 'content', 'cover')

# Register your models here.

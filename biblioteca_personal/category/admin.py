from django.contrib import admin

# Register your models here.
from category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    list_display = ('id', 'category')

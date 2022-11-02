from django.contrib import admin

# Register your models here.
from book.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin."""
    list_display = ('id', 'title', 'price', 'librero', 'id_author', 'id_category', 'rating','comment')
    


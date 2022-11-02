from unicodedata import category
from django.contrib import admin

# Register your models here.
from author.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin."""
    list_display = ('id', 'full_name')
    
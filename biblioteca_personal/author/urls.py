from django.urls import path
from author import views


urlpatterns = [
    path(
        route='list_author',
        view=views.list_author,
        name='list_author'
    ),
    path(
        route='add_author',
        view=views.add_author,
        name='add_author'
        ),
    path(
        route='delete_author/<int:pk>',
        view=views.delete_author,
        name='delete_author'
    ),
    path(
        route='edit_author/<int:pk>',
        view=views.edit_author,
        name='edit_author'
    ),
]
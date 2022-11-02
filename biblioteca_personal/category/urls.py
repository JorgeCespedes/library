from django.urls import path
from category import views


urlpatterns = [
    path(
        route='add_category',
        view=views.add_category,
        name='add_category'
        ),
    path(
        route='list_category',
        view=views.list_category,
        name='list_category'
    ),
    path(
        route='delete_category/<int:pk>',
        view=views.delete_category,
        name='delete_category'
    ),
    path(
        route='edit_category/<int:pk>',
        view=views.edit_category,
        name='edit_category'
    ),
]

from django.urls import path
from book import views


urlpatterns = [
    path(
        route='',
        view=views.home,
        name='home'
        ),
    
    path(
        route='list_book',
        view=views.list_book,
        name='list_book'
    ),
    path(
        route='add_book',
        view=views.add_book,
        name='add_book'
        ),
    path(
        route='delete_book/<int:pk>',
        view=views.delete_book,
        name='delete_book'
    ),
    path(
        route='edit_book/<int:pk>',
        view=views.edit_book,
        name='edit_book'
    ),
    
    path(
    route='detail_book/<int:pk>',
    view=views.detail_book,
    name='detail_book'
    ),
    
    path(
    route='about',
    view=views.about,
    name='about'
    ),
    
    path(
    route='report_status',
    view=views.report_status,
    name='report_status'
    )
    
    ]


from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('books_list/', views.books_list, name='book-list'),
    path('random_book/', views.random_book),
    path('random_book_with_missing/', views.random_book_with_missing),
    path('custom_path/<str:sub_path>/', views.get_path),
    path('books/<int:book_id>/', views.get_book_detail),
]
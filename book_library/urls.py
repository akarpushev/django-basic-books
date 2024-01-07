"""
URL configuration for book_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import index, about_handler, books_list, random_book, random_book_with_missing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about_handler),
    path('books_list/', books_list),
    path('random_book/', random_book),
    path('random_book_with_missing/', random_book_with_missing)
]

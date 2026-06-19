from django.urls import path

from core import views

urlpatterns = [path("books/", views.get_books)]

from django.urls import path

from .views import listview, details

app_name = "books"
urlpatterns = [

    path("books/", listview, name="list"),
    path("books/<int:book_id>", details, name="details"),

]

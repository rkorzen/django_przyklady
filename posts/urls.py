from django.urls import path

from .views import listview

app_name = "posts"
urlpatterns = [
    path("", listview, name="list"),  # /posts/
]

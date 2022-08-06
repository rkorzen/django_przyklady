from django.urls import path

from articles.views import author_details

urlpatterns = [

    path("authors/<int:author_id>/", author_details, name="author_details"),

]

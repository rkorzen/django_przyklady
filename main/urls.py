from django.urls import path

from .views import homepage, greetings

urlpatterns = [

    path("", homepage, name='homepage'),
    path("greetings/", greetings),

    path("greetings/<name>", greetings),
    # path("books/", greetings),

]

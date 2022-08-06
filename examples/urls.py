"""examples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from books.views import listview
from posts.views import listview as postslistview
from main.views import homepage, greetings

# /greetings/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('articles.urls')),
    path("", include("main.urls")),

    # można tak bardzo ogólnie przerzucić szukanie do innego urls
    path("", include("books.urls")),

    # można dać przedrostek - wspolny dla wszystkich wzorcow
    # z urls ktory inkludujemy
    path("posts/", include("posts.urls")),   # /posts/
    # /articles/
    # /authors/

]

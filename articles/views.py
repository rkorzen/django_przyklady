from django.shortcuts import render

# Create your views here.
from articles.models import Author


def author_details(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(
        request=request,
        template_name="authors/details.html",
        context={'author': author}
    )
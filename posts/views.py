from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# posts/
def listview(request):
    return render(
        request=request,
        template_name="posts/list.html"
    )
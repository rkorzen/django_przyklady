from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def homepage(request):
    # with open("templates/homepage.html") as f:
    #     html=f.read()

    # template = loader.get_template("homepage.html")
    # context = {"dane":[1, 2, 3]}
    # return HttpResponse(template.render(context, request))

    return render(
        request,
        "homepage.html",
        {
            "dane": "ALA MA KOTA",
            "a_list": [1, 2, 3],
            "author": {"name": "Adam", "last_name": "Mickiewicz"}
        }
    )

def greetings(request, name=""):
    return HttpResponse("Hello" + " " + name)

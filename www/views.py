from django.shortcuts import render


def index(request):
    context = {
        "message": "Hello from view!",
    }
    return render(request, "www/index.html", context)

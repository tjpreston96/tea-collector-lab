from django.shortcuts import render


# Create your views here.

# define the home view
def home(request):
    return HttpResponse("<h1>hello</h1>")


def about(request):
    return render(request, "about.html")

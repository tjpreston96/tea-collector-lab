from .models import Tea
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

# define the home view
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def teas_index(request):
    teas = Tea.objects.all()
    return render(request, "teas/index.html", {"teas": teas})


def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    return render(request, "teas/detail.html", {"tea": tea})


class TeaCreate(CreateView):
    model = Tea
    fields = "__all__"
    success_url = "/teas/"


class TeaUpdate(UpdateView):
    model = Tea
    fields = "__all__"

class TeaDelete(DeleteView):
    model = Tea
    success_url = '/teas/'


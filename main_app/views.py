from .models import Tea, Cup
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SweeteningForm


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
    # render to template
    sweetening_form = SweeteningForm()
    cups_tea_doesnt_have = Cup.objects.exclude(id__in=tea.cups.all().values_list("id"))
    return render(
        request,
        "teas/detail.html",
        {"tea": tea, "sweetening_form": sweetening_form, "cups": cups_tea_doesnt_have},
    )


def add_sweetening(request, tea_id):
    # create a ModelForm instance using the data in request.POST
    form = SweeteningForm(request.POST)
    # validate the form
    if form.is_valid():
        #  don't save the form to the db until it
        # has the tea_id assigned
        new_sweetening = form.save(commit=False)
        new_sweetening.tea_id = tea_id
        new_sweetening.save()
    return redirect("detail", tea_id=tea_id)


class TeaCreate(CreateView):
    model = Tea
    fields = "__all__"
    success_url = "/teas/"


class TeaUpdate(UpdateView):
    model = Tea
    fields = "__all__"


class TeaDelete(DeleteView):
    model = Tea
    success_url = "/teas/"


class CupList(ListView):
    model = Cup


class CupDetail(DetailView):
    model = Cup


class CupCreate(CreateView):
    model = Cup
    fields = "__all__"


class CupUpdate(UpdateView):
    model = Cup
    fields = ["name", "color"]


class CupDelete(DeleteView):
    model = Cup
    success_url = "/cups/"

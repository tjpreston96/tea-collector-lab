from .models import Tea, Cup
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SweeteningForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

# define the home view
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def teas_index(request):
    teas = Tea.objects.filter(user=request.user)
    return render(request, "teas/index.html", {"teas": teas})

@login_required
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

@login_required
def assoc_cup(request, tea_id, cup_id):
    Tea.objects.get(id=tea_id).cups.add(cup_id)
    return redirect("detail", tea_id=tea_id)

@login_required
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


class TeaCreate(LoginRequiredMixin, CreateView):
    model = Tea
    fields = "__all__"
    success_url = "/teas/"

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class TeaUpdate(LoginRequiredMixin, UpdateView):
    model = Tea
    fields = "__all__"


class TeaDelete(LoginRequiredMixin, DeleteView):
    model = Tea
    success_url = "/teas/"


class CupList(LoginRequiredMixin, ListView):
    model = Cup


class CupDetail(LoginRequiredMixin, DetailView):
    model = Cup


class CupCreate(LoginRequiredMixin, CreateView):
    model = Cup
    fields = "__all__"


class CupUpdate(LoginRequiredMixin, UpdateView):
    model = Cup
    fields = ["name", "color"]


class CupDelete(LoginRequiredMixin, DeleteView):
    model = Cup
    success_url = "/cups/"


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)

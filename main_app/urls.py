from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("teas/", views.teas_index, name="index"),
    path("teas/<int:tea_id>/", views.teas_detail, name="detail"),
    path("teas/create/", views.TeaCreate.as_view(), name="teas_create"),
    path("cats/<int:pk>/update/", views.TeaUpdate.as_view(), name="teas_update"),
    path("cats/<int:pk>/delete/", views.TeaDelete.as_view(), name="teas_delete"),
    path(
        "teas/<int:tea_id>/add_sweetening/", views.add_sweetening, name="add_sweetening"
    ),
    path(
        "teas/<int:tea_id>/assoc_cup/<int:cup_id>/", views.assoc_cup, name="assoc_cup"
    ),
    path("cups/", views.CupList.as_view(), name="cups_index"),
    path("cups/<int:pk>/", views.CupDetail.as_view(), name="cups_detail"),
    path("cups/create/", views.CupCreate.as_view(), name="cups_create"),
    path("cups/<int:pk>/update/", views.CupUpdate.as_view(), name="cups_update"),
    path("cups/<int:pk>/delete/", views.CupDelete.as_view(), name="cups_delete"),
    path("accounts/signup/", views.signup, name="signup"),
]
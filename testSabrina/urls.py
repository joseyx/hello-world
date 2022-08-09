from django.urls import path
from .views import sabrinaView, valuView

urlpatterns=[
    path("", sabrinaView, name="home"),
    path("valu/", valuView, name="valu"),
]
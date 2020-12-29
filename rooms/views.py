from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})

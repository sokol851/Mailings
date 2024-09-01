from django.shortcuts import render
from django.views.generic import ListView

from users.models import User


class UsersListView(ListView):
    model = User

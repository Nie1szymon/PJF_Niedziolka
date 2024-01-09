from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.contrib.auth.models import User, Group


def users_view(request):
    users = User.objects.all()
    groups = Group.objects.all()

    return render(request, 'registration/users_view.html', {
        'users': users,
        'groups': groups,
    })
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

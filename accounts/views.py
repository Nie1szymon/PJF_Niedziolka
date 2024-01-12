from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect

from django.contrib.auth.models import User, Group



def users_view(request):
    users = User.objects.all()
    groups = Group.objects.all()

    context = {
        'users': users,
        'groups': groups
    }

    if request.method == 'POST':
        group_ids = request.POST.getlist('groups')
        user_id = request.POST.get('user_id')

        user = User.objects.get(id=user_id)
        for group_id in group_ids:
            group = Group.objects.get(id=group_id)
            user.groups.add(group)

        user.save()

        context['message'] = f"User groups successfully updated for user {user.username}"

    return render(request, 'registration/users_view.html', context)


def change_group(request, user_id):
    user = User.objects.get(id=user_id)
    group_ids = request.POST.getlist('groups')

    for group_id in group_ids:
        group = Group.objects.get(id=group_id)
        user.groups.add(group)

    user.save()

    return redirect('listofuser/')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

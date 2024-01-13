from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User, Group

def user_belongs_to_Manager(user):
    return user.is_authenticated and (user.groups.filter(name='Manager').exists() or user.is_staff)

#@user_passes_test(user_belongs_to_Manager)
def users_view(request):
    users = User.objects.all()
    groups = Group.objects.all()

    context = {
        'users': users,
        'groups': groups
    }

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        group_ids = request.POST.getlist('groups[]')

        user.groups.set(group_ids)
        user.save()

        context['message'] = f"User groups successfully updated for user {user.username}"

    return render(request, 'registration/users_view.html', context)

@user_passes_test(user_belongs_to_Manager)
def change_group(request, user_id):
    user = get_object_or_404(User, id=user_id)
    groups = Group.objects.all()

    if request.method == 'POST':
        group_ids = request.POST.getlist('groups[]')
        user.groups.set(group_ids)
        user.save()

        return HttpResponseRedirect(reverse('listofuser'))
    return render(request, '/accounts/listofuser/', {'user': user, 'groups': groups})




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

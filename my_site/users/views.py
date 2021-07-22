from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewUserForm


def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, level=messages.SUCCESS, message="New User Created!")

            return redirect("users-login")

    else:
        form = NewUserForm()

    return render(request, template_name="users/register.html", context={'form': form})


@login_required
def profile(request):
    return render(request, template_name="users/profile.html", context={"title": "Profile"})


import ntpath
import os
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile
from .tasks import solveit


def signup(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get("username")
            raw_password = user_form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            try:
                profile = user.profile
            except Profile.DoesNotExist:
                profile = Profile(User=user)

            os.makedirs("users/%s/data" % profile.uid)
            os.makedirs("users/%s/schedules" % profile.uid)
            return redirect("profile")
    else:
        user_form = SignUpForm()

    return render(request, "signup.html", {"user_form": user_form})


@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("home")


def home(request):
    return render(request, "home.html")


@login_required(login_url="/login/")
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("home")

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, "profile.html", {"user_form": user_form,
                  "profile_form": profile_form})


@login_required(login_url="/login/")
def file_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)


    files = os.listdir("users/%s/data/" % profile.uid)
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            user_file = request.FILES['file']
            print()
            path = user_file.name
            head, tail = ntpath.split(path)
            path = tail or ntpath.basename(head)
            path = "users/%s/data/%s" % (profile.uid, path)
            print(path)

            with open(path, "wb+") as f:
                for chunk in user_file.chunks():
                    f.write(chunk)

                return redirect("/files/")
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form, "files": files})

@login_required(login_url="/login")
def schedule_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == "GET":
        path = "users/%s/data/data.dat" % profile.uid
        print(path)
        resdict = solveit.delay(path)
        solved = resdict.get()

        return render(request, "schedule.html", {"res": solved})
        mystr = ""
        for key,val in solved.items():
            mystr += "<p>"
            mystr += key
            mystr += ": "
            mystr += val
            mystr += "</p>"
        return HttpResponse("<html><body>" + mystr + 
                            "</body></html>")

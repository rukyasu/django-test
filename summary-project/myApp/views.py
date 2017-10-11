from django.shortcuts import render
from myApp.models import Player
from myApp.forms import NewPlayerForm, UserProfileInfoForm, UserForm
# Login functionality import
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    myDict = {
        "intro": "Welcome to the homepage!",
        "users": "Go to /players to see user list.",
    }
    return render(request, 'myApp/index.html', context=myDict)


def players(request):
    player_list = Player.objects.order_by('first_name')
    user_dict = {'users': player_list}
    return render(request, 'myApp/players.html', context=user_dict)


def register(request):
    player_form = NewPlayerForm()

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        player_form = NewPlayerForm(data=request.POST)

        if player_form.is_valid():
            player_form.save(commit=True)
            return index(request)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
            print("Error, the form is invalid!")

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "myApp/register.html", {
        "player_form": player_form,
        "user_form": user_form,
        "profile_form": profile_form,
        "registered": registered
        })


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed.")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'myApp/login.html', {})


@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

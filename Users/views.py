from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from forms import UserForm
from models import UserProfile
from Data.models import MetaStats
from interactions import UpdateChecker
# Create your views here.


def signup(request):
    #http://stackoverflow.com/questions/21107655/using-django-registration-with-a-flat-ui-template
    #http://stackoverflow.com/questions/2339369/how-can-i-override-the-django-authenticationform-input-css-class
    #http://stackoverflow.com/questions/1453488/how-to-markup-form-fields-with-div-class-field-type-in-django/1504903#1504903
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
        user.set_password(user.password)

        #created django user
        user.save()

        #created racehub user, link django user to it
        new_racehub_user = UserProfile(user=user)
        new_racehub_user.save()

        registered = True

    else:
        user_form = UserForm()

    context_dict = {'user_form': user_form, 'registered': registered}

    return render_to_response('signup.html', context_dict, context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                #login successful, check if data for user is synced
                #user_object = UserProfile.objects.get(user=user)
                #meta_stats = MetaStats.objects.get(default_id=1)
                #race_id = meta_stats.latest_race_id
                #update_checker = UpdateChecker(user_object=user_object, race_id=race_id)

                return HttpResponseRedirect('/main/home/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            correct_values = False
            return render_to_response('login.html', {'correct_values': correct_values}, context)
    else:
        correct_values = True
        return render_to_response('login.html', {'correct_values': correct_values}, context)


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/users/login/')


def team_page(request):
    pass


def settings(request):
    pass

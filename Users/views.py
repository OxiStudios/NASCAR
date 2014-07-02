from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from forms import UserForm
# Create your views here.


def signup(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()

        user.set_password(user.password)
        user.save()
        registered = True
    else:
        user_form = UserForm()

    context_dict = {'user_form': user_form, 'registered': registered}

    return render_to_response('Users/signup.html', context_dict, context)


def settings(request):
    pass


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/home/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('Users/login.html', {}, context)
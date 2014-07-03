from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Racers, RaceTrack
import models
# Create your views here.


def driver_home(request):
    context = RequestContext(request)
    context_dic = {}
    return render_to_response('main/driver_pages/driver_home.html', context_dic, context)


def driver(request, id="1"):
    context = RequestContext(request)
    driver_data = Racers.objects.get(number=id)
    context_dic = {'name': driver_data.name,
                   'points': driver_data.points}
    return render_to_response('driver.html', context_dic, context)


def test(request):
    context = RequestContext(request)
    context_dic = {'message': "What up son?!"}
    return render_to_response('test_2.html', context_dic, context)

def test_2(request):
    context = RequestContext(request)
    context_dic = {'message': "Test_2 bitch!!"}
    return render_to_response('test_2.html', context_dic, context)


def home_page(request):
    context = RequestContext(request)

    context_dic = {}
    return render_to_response('index.html', context_dic, context)


def data_input(request):
    context = RequestContext(request)

    if request.method == 'POST':
        if 'add_racer' in request.POST:
            number = request.POST['number']
            name = request.POST['name']
            points = request.POST['points']

            r = Racers(number=number, name=name, points=points)
            r.save()
            return render_to_response('data_saved.html', {}, context)
        elif 'add_track' in request.POST:
            track_id = request.POST['track_id']
            location = request.POST['location']
            track_length = request.POST['track_length']

            t = RaceTrack(track_id=track_id, location=location, track_length=track_length)
            t.save()
        else:
            pass
    else:
        return render_to_response('data_input.html', {}, context)

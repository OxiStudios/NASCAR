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

    #create list of racers that still need racing data saved
    racer_raw_list = Racers.objects.all()
    racer_list = []
    for racer in racer_raw_list:
        if racer.data_added == 0:
            racer_list.append(racer)

    #creat list of tracks
    track_list = RaceTrack.objects.all()

    #create content for the html page
    context_dic = {'racer_list': racer_list, 'track_list': track_list}

    if request.method == 'POST':
        if 'add_racer' in request.POST:
            number = request.POST['number']
            name = request.POST['name']
            points = request.POST['points']
            wins = request.POST['wins']

            r = Racers(number=number, name=name, points=points, wins=wins, data_added=0)
            r.save()
            return render_to_response('data_saved.html', {}, context)

        elif 'add_track' in request.POST:
            location_name = request.POST['location_name']
            track_length = request.POST['track_length']

            t = RaceTrack(location_name=location_name, track_length=track_length)
            t.save()
            return render_to_response('data_saved.html', {}, context)

        elif 'remove_racer' in request.POST:
            racer_to_remove = request.POST['racers']
            r = Racers.objects.get(number=racer_to_remove)
            r.delete()
            return render_to_response('data_saved.html', {}, context)

        else:
            pass

    else:
        return render_to_response('data_input.html', context_dic, context)

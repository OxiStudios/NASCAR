from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Racers
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
    return render_to_response('main/driver_pages/driver.html', context_dic, context)


def test(request):
    context = RequestContext(request)
    context_dic = {'message': "What up son?!"}
    return render_to_response('test/test_2.html', context_dic, context)

def test_2(request):
    context = RequestContext(request)
    context_dic = {'message': "Test_2 bitch!!"}
    return render_to_response('test/test_2.html', context_dic, context)


def home_page(request):
    context = RequestContext(request)

    context_dic = {}
    return render_to_response('main/index.html', context_dic, context)

def input_racer(request):
    context = RequestContext(request)

    if request.method == 'POST':
        number = request.post['number']
        name = request.post['name']
        points = request.post['points']
        r = Racers(number=number, name=name, points=points)
        r.save()

    else:
        return render_to_response('DataInput/racer_data_input.html', {}, context)

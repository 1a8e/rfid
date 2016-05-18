from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Scroll

def scroll(request):
	return HttpResponse("Hello, world from pigeon!")

def publish(request, scroll_id):
    thescroll = Scroll.objects.filter(scrollID=scroll_id)
    if len(thescroll):
    	thescroll = thescroll[0]
    else:
    	thescroll = None
    template = loader.get_template('pigeon/publish.html')
    context = {'scroll': thescroll}
    return HttpResponse(template.render(context, request))

def detail(request, scroll_id):
    response = "You're looking at scroll %s details."
    return HttpResponse(response % scrollID)
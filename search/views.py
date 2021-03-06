# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import urllib
# Create your views here.
def index(request):
	return render_to_response('search/index.html', {'aprovado' : 'hue'}, context_instance=RequestContext(request))

def result(request):
	name = ""
	if request.method == 'POST': # If the form has been submitted...
		name = request.POST.get('nome','') # A form bound to the POST data
		url = "http://vestibular.ufrgs.br/cv2015/lista_de_classificados/letra_" + name[0] + ".html"
		page = urllib.urlopen(url)
		page = page.read()
		page = page.decode('iso-8859-1').encode('utf8')
		name = name.encode('utf8')
		ok = page.find(name)
		if ok > 0:
			return render_to_response('search/index.html', {'aprovado': 'true', 'nome' : name }, context_instance=RequestContext(request))
		else:
			return render_to_response('search/index.html', {'aprovado': 'false', 'nome' : name }, context_instance=RequestContext(request))

def contact(request):
	return HttpResponse("Em construção")

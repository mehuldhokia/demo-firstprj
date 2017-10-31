# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse	# my code

# Create your views here.
def index(request):
	return HttpResponse("<h1>Hello, Django!!!</h1><h3>My first live website.</h3>")
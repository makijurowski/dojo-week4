# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse('Hey!')

def dog(request):
    return render(request, 'New_App/index.html')

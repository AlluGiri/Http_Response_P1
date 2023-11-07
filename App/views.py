from django.shortcuts import render
from django.http import HttpResponse 

def Prasanth(request):
    return HttpResponse('<h1><marquee>Prasanth is always Learning </h1></marquee>')

def Priya(request):
    return HttpResponse('<h1><marquee>Priya is always Eating and Sleeping</h1></marquee>')

def Giri(request):
    return HttpResponse('<h1><marquee>Giri is always .....?</h1></marquee>')

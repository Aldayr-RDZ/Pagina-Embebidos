from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("""
    <h1>Control de Alarma</h1>
    <h2> idAlarma </h2>
    <h2>Estado de Alarma</h2>
    """)




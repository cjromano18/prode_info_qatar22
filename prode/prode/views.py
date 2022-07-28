from urllib import request
from django.shortcuts import render


def inicio(request):
    template_name="inicio.html"
    usuario={
        "nombre": "Cristian",
        "apellido":"Romano"
    }
    ctx={
        "user_dic": usuario
    }
    return render(request, template_name, ctx)
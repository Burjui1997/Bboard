from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb


def index(request):
    bbs = Bb.objects.order_by("-published")
    return render(request, "bboard/index.html", {"bbs": bbs})

    # s = 'Обьявления\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by("-published"):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # Create your views here.

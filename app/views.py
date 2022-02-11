from random import randint
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import TemplateView

from app.models import Number
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "app/main.html"


@login_required(login_url='')
def logic(request):
    return render(request, 'app/logic.html')


# def system(request):
#     return render(request, 'app/system.html')

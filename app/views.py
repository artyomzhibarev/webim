from random import randint

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import TemplateView

from app.models import Number
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "app/main.html"


# def index(request):
#     return render(request, 'app/main.html', context={
#         'user': request.user,
#     })


@login_required(login_url='')
def logic(request):
    if request.is_ajax() and request.method == 'POST':
        number = randint(0, 9999)
        Number.objects.create(value=number)
        num = Number.objects.last().value
        return JsonResponse(data={'random_number': num}, status=200)
    return render(request, 'app/logic.html')

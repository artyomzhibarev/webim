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
    # num = Number.objects.last().value
    Number.objects.create(value=randint(0, 9999))
    num = Number.objects.last()
    if request.is_ajax() and request.method == 'POST':
        return JsonResponse(data={'random_number': num}, status=200)
    return render(request, 'app/logic.html', context={'random_number': num})

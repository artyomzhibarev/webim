from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render
from app.redis_server import redis_instance
# from app.management.commands.num_gen import singleton


class HomePageView(TemplateView):
    template_name = "app/main.html"


@login_required(login_url='')
def logic(request):
    if request.method == 'GET':
        try:
            rand_num = int(redis_instance.get('rand_num'))
        except TypeError:
            print(f"int() argument must be a string, a bytes-like object or a number, not {rand_num.__class__.__name__}")
            rand_num = 0
        finally:
            return render(request, 'app/logic.html',
                          context={'random_number': rand_num})
    return render(request, 'app/logic.html')

# def system(request):
#     return render(request, 'app/system.html')

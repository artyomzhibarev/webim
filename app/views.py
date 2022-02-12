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
            print(f"int() argument must be a string, a bytes-like object or a number, not NoneType")
            print(21)
            return render(request, 'app/logic.html',
                          context={'random_number': 0})
        else:
            print(25)
            return render(request, 'app/logic.html',
                          context={'random_number': rand_num})
    print(28)
    return render(request, 'app/logic.html')

# def system(request):
#     return render(request, 'app/system.html')

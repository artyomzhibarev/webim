from django.urls import path
from app.views import logic, HomePageView

app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logic/', logic, name='logic'),
]

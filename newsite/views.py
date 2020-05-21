from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Attraction

def index(request):
    attraction_list = Attraction.objects.order_by('name')
    context = {'attraction_list' : attraction_list}
    return render(request, 'newsite/attraction_list.html', context)
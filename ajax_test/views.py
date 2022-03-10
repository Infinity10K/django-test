from django.http import JsonResponse
from django.shortcuts import render
import datetime
import json

from .models import *

def index(request):

    time_now = datetime.datetime.now()
    products = Products.objects.all()

    context = {
        'title': 'Main Page',
        'time_now': time_now,
        'products': products
    }


    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'time_now': str(time_now),
            'table': list(products.values()),
        }

        return JsonResponse(data=data)

    return render(request, 'ajax_test/main.html', context=context)
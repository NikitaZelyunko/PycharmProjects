from django.shortcuts import render
from .models import WineItem
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['POST'])
def create_db(request):
    WineItem.objects.all().delete()
    bulc = []
    for item in request.data:
        print(item['inStock'])
        bulc.append(WineItem(
            item['index'],
            item['inStock'],
            item['price'][1:],
            item['picture'],
            item['year'],
            item['color'],
            item['type'],
            item['city'],
            item['name'],
            item['company'],
            item['about'],
            item['tags'][0]))

    WineItem.objects.bulk_create(bulc)

    return Response('OK', status=201)
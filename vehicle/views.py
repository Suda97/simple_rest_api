import json
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import requests
from .models import Vehicle


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def cars(request):
    if request.method == 'GET':
        # Saving in variable list of all objects in table Vehicle
        listOfCars = list(Vehicle.objects.values('id', 'make', 'model', 'avg_rating').order_by('id'))

        # Returning list of all cars as json
        return JsonResponse(listOfCars, safe=False)

    elif request.method == 'POST':
        req = json.loads(request.body)
        make, model = req['make'], req['model']
        car = list(Vehicle.objects.filter(make=make, model=model))

        if not car:
            # Saving list of cars with given maker
            url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
            r = (requests.get(url)).json()

            for line in r['Results']:
                if line['Model_Name'] == model:
                    Vehicle.objects.create(make=make, model=model, avg_rating=0, rates_number=0)
                    return HttpResponse()

            raise Http404('Make or model not found in external API')
        return HttpResponse('Model already in database\n')


@require_http_methods(['GET'])
def popular(request):
    # Getting list of all cars from database
    listOfCars = list(Vehicle.objects.values('id', 'make', 'model', 'rates_number').order_by('-rates_number'))

    # Returning list of cars as json
    return JsonResponse(listOfCars, safe=False)


@csrf_exempt
@require_http_methods(['DELETE'])
def delete(request, car_id):
    # Handling "Not found error"
    get_object_or_404(Vehicle, pk=car_id)
    Vehicle.objects.filter(id=car_id).delete()
    return HttpResponse()


@csrf_exempt
@require_http_methods(['POST'])
def rate(request):
    req = json.loads(request.body)
    car_id, rating = req['car_id'], req['rating']

    if rating > 5 or rating < 1:
        return HttpResponse('Rating should be ranging from 1 to 5')

    # Another way of handling "not found" error
    get_object_or_404(Vehicle, pk=car_id)

    data = Vehicle.objects.get(id=car_id)

    # Calculating new value of average rating for given car id
    new_avg_rating = float("{:.2f}".format((data.avg_rating * data.rates_number + rating) / (data.rates_number + 1)))
    data.avg_rating = new_avg_rating
    data.rates_number = data.rates_number + 1
    data.save()

    return HttpResponse()

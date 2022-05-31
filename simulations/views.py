from sys import api_version
from django.http import JsonResponse
from requests import Response
from .models import Simulation
from .serializers import SimulationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def simulation_list(request):
    if request.method == 'GET':
        simulations = Simulation.objects.all()
        serializer = SimulationSerializer(simulations, many=True)
        return JsonResponse({'simulations': serializer.data})

    if request.method == 'POST':
        serializer = SimulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED);

@api_view(['GET', 'PUT', 'DELETE'])
def simulation_detail(request, id):
    try:
        simulation = Simulation.objects.get(pk=id)
    except Simulation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SimulationSerializer(simulation)
        return Response(serializer.data)
    elif request.method == 'POST': 
        pass
    elif request.method == 'DELETE':
        pass

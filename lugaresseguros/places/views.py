from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from lugaresseguros.places import serializers
from places.models import Place
from places.serializers import PlaceSerializer

class PlaceView(APIView):
    def get(self, request):
        #Queryset es un conjunto de peticiones. 
        #es l conjunto de datos que almacena una query
        #una lista de datos. query peticion, queryset respuesta
        places = Place.objects.all()
        print(places)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlaceSingleView(APIView):
    def put(self, request, id):
        place = Place.objects.get(id=id)#el modelo oject tiene un id y 
        #yo lo comparo con lo que tengo
        serializer = PlaceSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        place = Place.objects.get(id=id)
        place.delete()
        return Response({"message":"Lugar eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

        


from rest_framework import serializers
from places.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__' #le decimos al serializador 
        #que serialice todos los atributos que tiene el modelo
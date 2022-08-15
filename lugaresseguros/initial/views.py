from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloDrf(APIView):
    def get(self, request, format=None): #request viaja la peticion hacia el servidor
        
        return Response({"message":"Hello world Drf!! :)"})

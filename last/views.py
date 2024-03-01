from rest_framework import generics
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car


class CarApi(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

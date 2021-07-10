from data import models
from rest_framework.generics import ListCreateAPIView
from .models import Cardata
from .serializers import CarSerializer


class CarGenericView(ListCreateAPIView):
    queryset = Cardata.objects.all()
    serializer_class = CarSerializer
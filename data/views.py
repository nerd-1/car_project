from rest_framework.viewsets import ModelViewSet
from .models import Cardata
from .serializers import CarSerializer


class CarGenericView(ModelViewSet):
    queryset = Cardata.objects.all()
    serializer_class = CarSerializer
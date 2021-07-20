from rest_framework.viewsets import ModelViewSet
from .models import Cardata, CardataRecord
from .serializers import CarRecordSerializer, CarSerializer

class CarGenericView(ModelViewSet):
    queryset = Cardata.objects.all()
    serializer_class = CarSerializer

class CarRecordGernericView(ModelViewSet):
    queryset = CardataRecord.objects.all()
    serializer_class = CarRecordSerializer
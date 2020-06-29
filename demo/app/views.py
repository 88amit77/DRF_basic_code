from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializers

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializers
from rest_framework import viewsets
from .models import Data
from rest_framework import filters
from .serializers import DataSerializers
from django_filters.rest_framework import DjangoFilterBackend

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('-id')
    serializer_class = DataSerializers
    # filterset_fields = ('name', 'city')
    # filter_fields = ('name', 'city')
    search_fields = ['name', 'city','occupation','age']
    ordering_fields = ['id']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
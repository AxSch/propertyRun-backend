from random import random

from rest_framework import viewsets
from houses.models import House, Viewer
from houses.serializers import HouseSerializer, ViewerSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ViewerAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer


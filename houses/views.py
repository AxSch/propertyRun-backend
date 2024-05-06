from random import random

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from houses.models import House, Viewer
from houses.serializers import HouseSerializer

class HouseViewSet(viewsets.ModelViewSet):
    def list(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def create(self, request):
        house_serializer = HouseSerializer(data=request.data)
        if house_serializer.is_valid():
            house_serializer.save()
            return Response(house_serializer.data, status=status.HTTP_201_CREATED)
        return Response(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        house = House.objects.get(pk=pk)
        house_serializer = HouseSerializer(house)
        return Response(house_serializer.data)

    def update(self, request, pk=None):
        house = House.objects.get(pk=pk)
        house_serializer = HouseSerializer(house, data=request.data)
        if house_serializer.is_valid():
            house_serializer.save()
            return Response(house_serializer.data, status=status.HTTP_200_OK)
        return Response(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        house = House.objects.get(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewerAPIView(APIView):
    def get(self, request):
        viewers = Viewer.objects.all()
        viewer = random.choice(viewers)
        return Response({
            'id': viewer.id,
        })


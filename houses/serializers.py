from rest_framework import serializers
from houses.models import House, Viewer

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = '__all__'
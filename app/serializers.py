from django.contrib.auth.models import User

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import Provider, ServiceArea


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone_number', 'language', 'currency']


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = serializers.CharField(source='provider.name', read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = "geojson"
        fields = ['id', 'name', 'price', 'geojson', 'provider']

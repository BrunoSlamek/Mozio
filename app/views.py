
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Provider, ServiceArea
from .serializers import UserSerializer, ProviderSerializer, ServiceAreaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['get'], url_path='search')
    def _search_lat_lng(self, request):
        """
        Custom endpoint that takes lat/lng as query params and returns
        all service areas (polygons) that contain the point.
        """
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')

        if lat is None or lng is None:
            return Response({'error': 'lat and lng are required parameters'}, status=status.HTTP_400_BAD_REQUEST)

        point = Point(float(lng), float(lat), srid=4326)
        service_areas = ServiceArea.objects.filter(geojson__contains=point)

        serializer = self.get_serializer(service_areas, many=True)
        return Response(serializer.data)

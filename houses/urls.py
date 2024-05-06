from django.urls import path
from .views import HouseViewSet, ViewerAPIView

urlpatterns = [
    path('houses/', HouseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='houses'),
    path('houses/<int:pk>/', HouseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('viewer', ViewerAPIView.as_view())
]
from rest_framework.viewsets import ModelViewSet
from .models import Facebook, ToDo
from .serializers import ToDoModelSerializer, FacebookModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class FacebookModelViewSet(ModelViewSet):
    queryset = Facebook.objects.all()
    serializer_class = FacebookModelSerializer

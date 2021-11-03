from rest_framework.serializers import ModelSerializer
from .models import Facebook, ToDo


class FacebookModelSerializer(ModelSerializer):
    class Meta:
        model = Facebook
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

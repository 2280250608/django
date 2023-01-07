from rest_framework import serializers
from .models import Example


class ExampleSerializer(serializers.ModelSerializer):
    """ Serializer of a show """

    class Meta:
        model = Example
        fields = '__all__'

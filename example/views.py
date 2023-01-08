from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import Example
from .serializers import ExampleSerializer


# Create your views here.


class ExampleView(APIView):
    def get(self, _request):
        print('*****************hi')
        # examples = Example.objects.all()
        # print(f'***************hi {examples}')
        serialized_example = ExampleSerializer()
        return Response(serialized_example.data)
        # return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

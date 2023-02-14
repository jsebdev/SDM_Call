from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from calls.models import Call
from .serializers import CallSerializer


# @api_view(['GET'])
# def getCalls(request):
#     calls = Call.objects.all()
#     serializer = CallSerializer(calls, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def call(request):
#     serializer = CallSerializer(data=request.data)
#     print('18: request.data >>>', request.data)
#     print('checking if is valid')
#     if serializer.is_valid(raise_exception=True):
#         print('saving')
#         serializer.save()
#     return Response(serializer.data)


@api_view(['GET', 'POST'])
def call(request):
    print('30: request.data >>>', request.data)
    print('28: request >>>', request.method)
    if request.method == 'POST':

        # data = JSONParser().parse(request)
        # serializer = CallSerializer(data=data)
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    if request.method == 'GET':
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)

    return Response({'message': 'methods not supported'})

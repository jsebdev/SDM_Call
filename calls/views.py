from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Call
from .serializers import CallSerializer


@api_view(['GET', 'POST'])
def call(request):
    # todo: make one call at a time, avoid making multiple calls to the model at the same time
    if request.method == 'POST':
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        print('15: type(data) >>>', type(data))
        call = Call.objects.get(id=data['id'])
        print('17: call >>>', call)
        results = call.generateResults()
        return Response({'results': results})
        # return Response({'image_url': 'doing testing'})

    if request.method == 'GET':
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)

    return Response({'message': 'method not supported'})

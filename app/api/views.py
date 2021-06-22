from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.models import UUIDModel
from .serializers import UUIDModelSerializer

class UUIDgenApiView(APIView):

    def get(self, request, *args, **kwargs):

        uid = UUIDModel.objects.all()
        serializer = UUIDModelSerializer(uid, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
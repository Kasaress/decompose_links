from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LinksSerializer


class LinksView(APIView):
    """Принимает и логирует ссылку."""

    def post(self, request):
        serializer = LinksSerializer(data=request.data)
        serializer.is_valid()
        if serializer.is_valid():
            return Response(
                'Ссылка залогирована',
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LinksSerializer

logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    filemode='a',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)


class LinksView(APIView):
    """Принимает и логирует ссылку."""

    def post(self, request):
        serializer = LinksSerializer(data=request.data)
        serializer.is_valid()
        if serializer.is_valid():
            logging.info(serializer.validated_data.get('link'))
            return Response(
                f"Ссылка в логе: {serializer.validated_data.get('link')}",
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

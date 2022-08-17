import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler

from .serializers import LinksSerializer


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response


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
        try:
            if serializer.is_valid():
                logging.info(serializer.validated_data.get('link'))
            return Response(
                f"Ссылка в логе: {serializer.validated_data.get('link')}",
                status=status.HTTP_200_OK)
        except serializer.errors:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(
            'Используйте POST-запрос на адрес "http://127.0.0.1:8000/api/v1/links/"')

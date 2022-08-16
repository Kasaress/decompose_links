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
            link_as_dick = {}
            try:
                link_as_dick['protocol'] = serializer.validated_data.get(
                    'link').split('://')[0]
            except IndexError:
                link_as_dick['protocol'] = 'null'

            try:
                link_as_dick['domen'] = serializer.validated_data.get(
                    'link').split('://')[1].split('/')[0]
            except IndexError:
                link_as_dick['domen'] = 'null'

            try:
                link_as_dick['path'] = serializer.validated_data.get(
                    'link').split('://')[1].split('/')[1].split('?')[0]
            except IndexError:
                link_as_dick['path'] = 'null'

            try:
                link_as_dick['params'] = serializer.validated_data.get(
                    'link').split('://')[1].split('/')[1].split('?')[1]
            except IndexError:
                link_as_dick['params'] = 'null'

            logging.info(link_as_dick)
            return Response(
                f'Ссылка залогирована: {link_as_dick}',
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=200)

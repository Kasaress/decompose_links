from urllib.parse import urlparse

from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=200)

    def validate_link(self, link):
        parsed_url = urlparse(link)
        link = dict(parsed_url._asdict())
        new_link = {}
        if link['path'].split('.')[-1].lower() == 'git':
            link['is_git'] = True
            link['git_name'] = link['path'].lower().split(
                    '.git')[0].split('/')[-1]
        for key in link:
            if link[key] != '':
                new_link[key] = link[key]
        link = new_link
        return link

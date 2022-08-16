from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=200)

    def validate_link(self, link):
        link_as_dick = {}
        try:
            link_as_dick['protocol'] = self.initial_data.get(
                    'link').split('://')[0]
        except IndexError:
            link_as_dick['protocol'] = 'null'

        try:
            link_as_dick['domen'] = self.initial_data.get(
                'link').split('://')[1].split('/')[0]
        except IndexError:
            link_as_dick['domen'] = 'null'

        try:
            link_as_dick['path'] = self.initial_data.get(
                'link').split('://')[1].split('/')[1].split('?')[0]
        except IndexError:
            link_as_dick['path'] = 'null'

        try:
            link_as_dick['params'] = self.initial_data.get(
                'link').split('://')[1].split('/')[1].split('?')[1]
        except IndexError:
            link_as_dick['params'] = 'null'
        link = link_as_dick
        return link

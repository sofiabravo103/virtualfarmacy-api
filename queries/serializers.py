from rest_framework import serializers
from queries.models import Query
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)



class QuerySerializer(TaggitSerializer,serializers.ModelSerializer):
    keywords = TagListSerializerField()

    class Meta:
        model = Query
        fields = ('created', 'intention', 'intersect_keywords', 'keywords')

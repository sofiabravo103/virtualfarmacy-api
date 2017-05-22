from rest_framework import serializers
from queries.models import Query

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('created', 'intention', 'intersect_keywords', 'keywords')

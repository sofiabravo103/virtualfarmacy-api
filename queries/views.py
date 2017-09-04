from rest_framework import generics
from queries.models import Query
from queries.serializers import QuerySerializer


class QueryList(generics.ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

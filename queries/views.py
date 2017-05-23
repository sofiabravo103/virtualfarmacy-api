from rest_framework.decorators import api_view
from rest_framework.response import Response
from queries.models import Query
from queries.serializers import QuerySerializer

# Create your views here.
@api_view(['GET', 'POST'])
def query_list(request):
    """
    List all code queries, or create a new query.
    """
    if request.method == 'GET':
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def query_detail(request, pk):
    """
    Retrieve, update or delete a query.
    """
    try:
        query = Query.objects.get(pk=pk)
    except Query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuerySerializer(query)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuerySerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

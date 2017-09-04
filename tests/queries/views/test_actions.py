import random
import string
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from queries.models import Query
from queries.serializers import QuerySerializer
from factories import QueryFactory


class QueryListTests(APITestCase):

    def test_create_query(self):
        '''Ensure we can create a new account object.'''

        url = reverse('queries-list')
        data = QuerySerializer(QueryFactory.stub()).data
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Query.objects.count() == 1
        assert Query.objects.get().intention, data['intention']
        assert Query.objects.get().keywords, data['keywords']
        assert Query.objects.get().intersect_keywords, data['intersect_keywords']

    def test_list_queries(self):
        '''Ensure we can list all queries'''

        list_size = random.choice(range(1,5))
        for _ in range(list_size):
            QueryFactory.create()

        url = reverse('queries-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == list_size

import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from queries.models import Query
from queries.serializers import QuerySerializer
from factories import QueryFactory, random_keyword_list


class QueryListTests(APITestCase):

    def test_create_query(self):
        '''Ensure we can create a new query object.'''

        url = reverse('queries-list')
        data = {
            'intention': random.choice(Query.INTENTION_CHOICES),
            'intersect_keywords': random.choice([True, False]),
            'keywords': random_keyword_list()
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Query.objects.count() == 1
        assert Query.objects.get().intention, data['intention']
        assert Query.objects.get().keywords, data['keywords']
        # assert Query.objects.get().intersect_keywords, data['intersect_keywords']

    def test_list_queries(self):
        '''Ensure we can list all queries'''

        list_size = random.choice(range(1,5))
        for _ in range(list_size):
            QueryFactory.create()

        url = reverse('queries-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == list_size


class QueryDetailTests(APITestCase):

    def test_get_query(self):
        '''Ensure we can get a query object.'''

        test_query = QueryFactory.create()

        url = reverse('query-detail', args=([test_query.id]))
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == QuerySerializer(test_query).data

    def test_edit_query(self):
        '''Ensure we can edit a query'''

        test_query = QueryFactory.create()
        url = reverse('query-detail', args=([test_query.id]))
        new_keywords = ['this', 'is', 'a', 'test']
        new_intention = random.choice(Query.INTENTION_CHOICES)
        test_query.keywords = new_keywords
        test_query.intention = new_intention
        data =  QuerySerializer(test_query).data
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        edited_tag_names = {tag.name for tag in Query.objects.get().keywords.all()}
        assert edited_tag_names == {'this', 'is', 'a', 'test'}
        assert Query.objects.get().intention == new_intention

    def test_delete_query(self):
        '''Ensure we can delete a query'''

        test_query = QueryFactory.create()
        url = reverse('query-detail', args=([test_query.id]))
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(Query.objects.all()) == 0

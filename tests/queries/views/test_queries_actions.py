import random
import pytest
import json
from django.urls import reverse
from rest_framework import status
from queries.models import Query
from queries.serializers import QuerySerializer
from tests.factories import QueryFactory, random_keyword_set

@pytest.mark.django_db
def test_create_query(client):
    '''Ensure we can create a new query object.'''

    url = reverse('queries-list')
    keywords = random_keyword_set()
    data = {
        'intention': random.choice(Query.INTENTION_CHOICES),
        'intersect_keywords': random.choice([True, False]),
        'keywords': json.dumps(list(keywords)),
        'public' : random.choice([True, False])
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Query.objects.count() == 1
    assert Query.objects.get().intention == data['intention']
    assert Query.objects.get().intersect_keywords == data['intersect_keywords']
    assert Query.objects.get().public == data['public']

    tag_names = {tag.name for tag in Query.objects.get().keywords.all()}
    assert tag_names == keywords

@pytest.mark.django_db
def test_list_queries(client):
    '''Ensure we can list all queries'''

    list_size = random.choice(range(1,5))
    for _ in range(list_size):
        QueryFactory.create()

    url = reverse('queries-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == list_size


@pytest.mark.django_db
def test_get_query(client):
    '''Ensure we can get a query object.'''

    test_query = QueryFactory.create()

    url = reverse('query-detail', args=([test_query.id]))
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == QuerySerializer(test_query).data


@pytest.mark.django_db
def test_edit_query(client):
    '''Ensure we can edit a query'''

    test_query = QueryFactory.create()

    keywords = random_keyword_set()
    data = {
        'intention': random.choice(Query.INTENTION_CHOICES),
        'keywords': json.dumps(list(keywords))
    }

    url = reverse('query-detail', args=([test_query.id]))
    response = client.put(url, json.dumps(data), content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    edited_tag_names = {tag.name for tag in Query.objects.get().keywords.all()}
    assert edited_tag_names == keywords
    assert Query.objects.get().intention == data['intention']


@pytest.mark.django_db
def test_delete_query(client):
    '''Ensure we can delete a query'''

    test_query = QueryFactory.create()
    url = reverse('query-detail', args=([test_query.id]))
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert len(Query.objects.all()) == 0

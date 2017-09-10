import random
import pytest
import json
from django.urls import reverse
from rest_framework import status
from queries.models import Query
from tests.factories import QueryFactory, random_keyword_set


@pytest.mark.django_db
def test_bad_request_with_inexisting_intention_choice(client):
    url = reverse('queries-list')
    keywords = random_keyword_set()
    data = {
        'intention': 'TS',
        'keywords': json.dumps(list(keywords)),
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.content == b'{"intention":["\\"TS\\" is not a valid choice."]}'


@pytest.mark.django_db
def test_bad_request_without_keywords(client):
    url = reverse('queries-list')
    data = {
        'intention': random.choice(Query.INTENTION_CHOICES),
        'intersect_keywords': random.choice([True, False]),
        'public' : random.choice([True, False])
    }
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.content == b'{"keywords":["This field is required."]}'

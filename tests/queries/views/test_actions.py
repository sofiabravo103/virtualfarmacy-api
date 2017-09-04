import random
import string
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from queries.models import Query


def random_keyword_list():

    def random_word():
        return ''.join(random.choices(string.ascii_letters, \
            k=random.choice(range(1,10))))

    return [random_word() for _ in range(random.choice(range(1,12)))]


class QueryListTests(APITestCase):

    def test_create_account(self):
        '''Ensure we can create a new account object.'''

        url = reverse('queries-list')
        data = {
            'intention': random.choice(Query.INTENTION_CHOICES),
            'keywords': random_keyword_list(),
            'intersect_keywords': random.choice([True, False])
        }
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
            Query.objects.create(
                intention=random.choice(Query.INTENTION_CHOICES),
                keywords=random_keyword_list(),
                intersect_keywords=random.choice([True, False])
            )

        url = reverse('queries-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == list_size

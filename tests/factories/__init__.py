import factory
import random
import string
from queries.models import Query

# To use faker:
# from faker import Factory as FakerFactory
# faker = FakerFactory.create()


def random_keyword_list():

    def random_word():
        return ''.join(random.choices(string.ascii_letters, \
            k=random.choice(range(1,10))))

    return [random_word() for _ in range(random.choice(range(1,12)))]

class QueryFactory(factory.django.DjangoModelFactory):
    """Query factory."""

    class Meta:
        model = Query

    # example for subfactory:
    # author = factory.SubFactory(AuthorFactory)

    intention = random.choice(Query.INTENTION_CHOICES)
    keywords = random_keyword_list()
    intersect_keywords = random.choice([True, False])

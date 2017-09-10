import factory
import random
import string
from queries.models import Query

# To use faker:
# from faker import Factory as FakerFactory
# faker = FakerFactory.create()


def random_keyword_set():

    def random_word():
        return ''.join(random.choices(string.ascii_letters, \
            k=random.choice(range(1,10))))

    return { random_word() for _ in range(random.choice(range(1,12)))}

class QueryFactory(factory.django.DjangoModelFactory):
    """Query factory."""

    class Meta:
        model = Query

    # example for subfactory:
    # author = factory.SubFactory(AuthorFactory)

    intention = random.choice(Query.INTENTION_CHOICES)
    intersect_keywords = random.choice([True, False])
    keywords = random_keyword_set()
    public = random.choice([True, False])


    # This is a fixture needed by django-taggit-serializer:
    # http://factoryboy.readthedocs.io/en/latest/recipes.html#simple-many-to-many-relationship
    @factory.post_generation
    def keywords(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of tags were passed in, use them.
            for tag in extracted:
                self.keywords.add(tag)

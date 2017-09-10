from django.db import models
from rest_framework import mixins
from taggit.managers import TaggableManager


class Query(models.Model):
    OFFER = 'OF'
    REQUEST = 'RE'
    INTENTION_CHOICES = [OFFER, REQUEST]
    INTENTION_CHOICES_NAMED = (
        (OFFER, 'Offer'),
        (REQUEST, 'Request')
    )
    created = models.DateTimeField(auto_now_add=True)
    intention = models.CharField(
        max_length=2,
        choices=INTENTION_CHOICES_NAMED
    )
    intersect_keywords = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    keywords = TaggableManager()


class Execution(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    auto = models.BooleanField(default=False)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)


class Result(models.Model):
    text_hash = models.CharField(max_length=32)
    from_twitter_status_id = models.CharField(max_length=64)
    useful = models.BooleanField(default=False)
    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    #source = models.ForeignKey(Source, on_delete=models.PROTECT)


class Alert(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    query = models.ForeignKey(Query, on_delete=models.CASCADE)

from django.db import models
from elixir.model.resource_model.resource import * 

class PublicationMetadata(models.Model):
    updated = models.DateTimeField(null=True, blank=True)
    title = models.TextField(blank=True, null=True)
    journal = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    citationCount = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.title) or u''



class Publication(models.Model):
    pmcid = models.TextField(blank=True, null=True)
    pmid = models.TextField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    resource = models.ForeignKey(Resource, null=True, blank=True, related_name='publication', on_delete=models.CASCADE)
    metadata = models.OneToOneField(PublicationMetadata, null=True, blank=True, related_name='publication', on_delete=models.CASCADE)

    # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.pmcid) or u''


class PublicationAuthor(models.Model):
    name = models.TextField(blank=True, null=True)
    metadata = models.ForeignKey(PublicationMetadata, null=True, blank=True, related_name='authors', on_delete=models.CASCADE)

    def __unicode__(self):
        return unicode(self.name) or u''
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


# we did the three lines after the `tag` to make a generic way to identify an object(general not specific):
# so that this app will be independent of any other app
class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we can identify any object in our app\ identify any record in any table by knowing 2 things:
    # 1- type(product, video, article) \ the table
    # 2- ID \ the record
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()  # using this field we can read the actual object that a particular tag is
    # applied to

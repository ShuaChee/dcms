from django.db import models
from cms.models.fields import PlaceholderField

class MyCoolModel(models.Model):
    my_placeholder = PlaceholderField('cool_placeholder')
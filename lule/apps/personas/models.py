from django.db import models
from datetime import date, datetime
# Models
from django.contrib.auth.models import User

from apps.personas.api.pictures.validators import bad_validator

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENCES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Publica'),
    (PRIVATE, 'Privada')
)


class Photo(models.Model):

    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, default="", validators=[bad_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENCES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY)

    # Llaves foraneas
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

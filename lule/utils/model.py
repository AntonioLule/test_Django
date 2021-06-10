from django.db import models


class BaseModelName(models.Model):
    """
    Establecemos la base para los modelos con nombre y fechas en sus elementos
    """

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

from django.core.exceptions import ValidationError
from django.conf import settings


def bad_validator(value):
    """
    Valida si en value se han puesto paralabras no permitidas
    :param value: Boolean
    :return:
    """

    for bad in settings.BAD:
        if bad.lower() in value.lower():
            raise ValidationError('La palabra {0} no esta permitida'.format(bad))

    # Si todo va ok, debuelvo True
    return True
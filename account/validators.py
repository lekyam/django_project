from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_adult(value):
    min_age = 18
    if (timezone.now().date() - value).days < min_age * 365:
        raise ValidationError('Debes tener al menos 18 años para registrarte')
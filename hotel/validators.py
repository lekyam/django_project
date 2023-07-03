from django.core.exceptions import ValidationError
from datetime import datetime

def validate_positive(value):
    if value <= 0:
        raise ValidationError('El valor no puede ser negativo')

def validate_date(value):
    if value is None:
        raise ValidationError("La fecha no es correcta.")
    try:
        date_string = value.strftime("%Y-%m-%d")
        datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        raise ValidationError("La fecha no es correcta.")

def validate_start_end_date(start, end):
    try:
        if start >= end:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")
    except ValueError:
        raise ValidationError("Las fechas proporcionadas son inválidas.") 
     
def validate_future_date(date):
    try:
        if date < datetime.today().date():
            raise ValidationError("La fecha debe ser en el futuro")
    except ValueError:
        raise ValidationError("Hay un error con la fecha.")

def validate_max_days_reservation(start_date,end_date):
    max_days = 5
    days = (end_date - start_date).days
    try: 
        if days > max_days:
            raise ValidationError("Solo se pueden reservar hasta 5 dias")
    except ValueError:
        print("Error max")
        raise ValidationError("Las fechas proporcionadas son inválidas.")
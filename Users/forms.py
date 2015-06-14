# -*- encoding: utf-8 -*-
from django.forms import ModelForm

from Users.models import Medic


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
# * MedicForm
# * PatientFrom


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Tablas de la base de datos
TABLES = {
    'Medic': 'medic_db_table',
    'Patient': 'patient_db_table',
}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Funciones para retornar la el tiempo utc actual separado en hora y fecha
class MedicFrom(ModelForm):
    class Meta:
        model = Medic
        fields = [
            'first_name',
            'last_name',
            'dni',
            'ndc',
            'password',
        ]

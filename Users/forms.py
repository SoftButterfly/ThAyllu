# -*- encoding: utf-8 -*-
from django.forms import ModelForm

from django.contrib.auth.models import User
from Users.models import Mother

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
# * LoginVisitorFrom
# * PatientFrom


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Funciones para retornar la el tiempo utc actual separado en hora y fecha
class LoginVisitorFrom(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class MotherForm(ModelForm):
    class Meta:
        model = Mother
        fields = [
            'DNI',
            'FirstName',
            'LastName',
            'BirthDate',
            'CivilState',
            'Ocupation',
            'PreviousPregnancies',
            'Provice',
            'District',
        ]

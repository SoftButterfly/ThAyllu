# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as baseUser


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
# * Medic
# * Patient


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Tablas de la base de datos
TABLES = {
    'Medic': 'medic_db_table',
    'Patient': 'patient_db_table',
}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Medic object
class Medic(baseUser):
    objectName = 'Medic'

    dni = models.IntegerField(
        "Documento de identidad",
        unique=True,
        blank=True,
        null=True
    )

    ndc = models.IntegerField(
        "Número de Colegiatura",
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Doctor'
        verbose_name = 'Doctores'

        db_table = TABLES['Medic']

    def save(self, *args, **kwargs):
        self.username = str(self.dni)

        super(Medic, self).save(*args, **kwargs)

    def __str__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe',
            'ndc': 'NN',
        }

        if self.ndc:
            fmt_data.update({'ndc': self.ndc})

        return 'Doctor {firstName:} {lastName:}, {ndc:}'.format(**fmt_data)

    def __unicode__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe',
            'ndc': 'NN',
        }

        if self.ndc:
            fmt_data.update({'ndc': self.ndc})

        return 'Doctor {firstName:} {lastName:}, {ndc:}'.format(**fmt_data)

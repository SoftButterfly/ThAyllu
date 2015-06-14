# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import date

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
# * vaccine
# * Vaccine Calendar


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Table:
TABLES = {
    'VaccineCalendar': 'vcalendar_db_table',
    'CredCalendar': 'cred_db_table',
}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Vaccine:
class VaccineCalendar(models.Model):
    objectName = 'Vaccine'

    # 0 meses
    BCG = 1
    HVB = 2

    # 2 meses
    PENTAI = 3
    APOI = 4
    ROTAVIRUSI = 4

    # 3 meses
    NEUMOCOCOI = 5

    # 4 meses
    PENTAII = 6
    APOII = 7
    ROTAVIRUSII = 8

    # 5 meses
    NEUMOCOCOII = 9

    # 6 meses
    APOIII = 10
    ROTAVIRUSIII = 11

    # 7 meses
    INFLUENZAI = 12

    # 8 meses
    INFLUENZAII = 13

    # 12 meses
    SRPI = 14
    NEUMOCOCOIII = 15

    # 15 meses
    ANTIAMARILLA = 16

    # 18 meses
    DPTI = 17

    # 48 meses
    SPRII = 18
    DPTII = 19

    VACCINE_TYPE = (
        (BCG, 'BCG'),
        (HVB, 'HVB'),
        (PENTAI, '1ra Pentavalente'),
        (APOI, '1ra Antipoliomelitis'),
        (ROTAVIRUSI, '1ra Rotavirus'),
        (NEUMOCOCOI, '1ra Neumococo'),
        (PENTAII, '2da Pentavalente'),
        (APOII, '2da Antipoliomelitis'),
        (ROTAVIRUSII, '2da Rotavirus'),
        (NEUMOCOCOII, '2da Neumococo'),
        (APOIII, '3ra Antipoliomelitis'),
        (ROTAVIRUSIII, '3ra Rotavirus'),
        (INFLUENZAI, '1ra Influenza'),
        (INFLUENZAII, '2da Influenza'),
        (SRPI, '1ra SRP'),
        (NEUMOCOCOIII, '3ra Neumococo'),
        (ANTIAMARILLA, 'Fiebre Amarilla'),
        (DPTI, '1er refuerzo DPT'),
        (SPRII, 'Refuerzo SPR'),
        (DPTII, '2do refuerzo DPT'),
    )

    Type = models.IntegerField(
        "Tipo de vacuna",
        choices=VACCINE_TYPE,
        default=BCG
    )

    YES = 0
    NO = 1

    APPLICATION_STATE = (
        (YES, 'Sí'),
        (NO, 'No'),
    )

    Applied = models.IntegerField(
        "Aplicada",
        choices=APPLICATION_STATE,
        default=NO,
    )

    ApplicationDate = models.DateField(
        "Fecha de aplicación"
        default=date.today
    )

    class Meta:
        verbose_name = 'Visitador'
        verbose_name = 'Visitadores'

        db_table = TABLES['Visitor']

    def save(self, *args, **kwargs):
        self.username = str(self.dni)
        super(Vaccine, self).save(*args, **kwargs)

    def __str__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe'
        }

        if self.first_name:
            fmt_data.update({'firstName': self.first_name})

        if self.last_name:
            fmt_data.update({'lastName': self.last_name})

        return 'Visitador(a) {firstName:} {lastName:}'.format(**fmt_data)

    def __unicode__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe'
        }

        if self.first_name:
            fmt_data.update({'firstName': self.first_name})

        if self.last_name:
            fmt_data.update({'lastName': self.last_name})

        return u'Visitador(a) {firstName:} {lastName:}'.format(**fmt_data)

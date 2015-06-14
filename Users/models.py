# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from datetime import date

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
# * Visitor
# * Patient
# * Child


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Tablas de la base de datos
TABLES = {
    'Visitor': 'visitor_db_table',
    'Mother': 'mother_db_table',
    'Child': 'child_db_table',
}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Visitor object
class Visitor(models.Model):
    DNI = models.IntegerField(
        "Documento de identidad",
        unique=True,
        primary_key=True
    )

    FirstName = models.CharField(
        "Nombre(s)",
        max_length=64,
    )

    LastName = models.CharField(
        "Apellido(s)",
        max_length=64,
    )

    password = models.CharField(
        "Contraseña",
        max_length=64,
    )

    asociatedUser = models.OneToOneField(
        User,
        editable=False,
        blank=True,
        null=True
    )

    Traveler0 = models.CharField(
        max_length=20,
        editable=False,
        blank=True
    )

    Traveler1 = models.CharField(
        max_length=20,
        editable=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Visitador'
        verbose_name_plural = 'Visitadores'

        db_table = TABLES['Visitor']

    def save(self, *args, **kwargs):
        if User.objects.filter(username=str(self.DNI)).exists():
            user = User.objects.filter(username=str(self.DNI))[0]
        else:
            user = User()

        user.username = str(self.DNI)
        user.set_password(self.password)
        user.first_name = self.FirstName
        user.last_name = self.LastName
        user.is_staff = True

        try:
            user.save()
            self.asociatedUser = user

            super(Visitor, self).save(*args, **kwargs)
        except:
            pass

    def __str__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return 'Visitador(a) {firstName:} {lastName:}'.format(**fmt_data)

    def __unicode__(self):
        fmt_data = {
            'firstName': 'Jhon',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return u'Visitador(a) {firstName:} {lastName:}'.format(**fmt_data)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Mother object
class Mother(models.Model):
    DNI = models.IntegerField(
        "Documento de identidad",
        unique=True
    )

    FirstName = models.CharField(
        "Nombre(s)",
        max_length=64,
    )

    LastName = models.CharField(
        "Apellido(s)",
        max_length=64,
    )

    BirthDate = models.DateField(
        "Fecha de nacimiento",
        default=date.today
    )

    SINGLE = 1
    MARRIED = 2
    DIVOCED = 3
    WIDOW = 4

    CIVILSTATE = (
        (SINGLE, "Soltera"),
        (MARRIED, "Casada"),
        (DIVOCED, "Divorciada"),
        (WIDOW, "Viuda"),
    )

    CivilState = models.IntegerField(
        "Estado civil",
        default=MARRIED
    )

    Ocupation = models.CharField(
        "Ocupación",
        max_length=64,
    )

    PreviousPregnancies = models.IntegerField(
        "Embarazos previos"
    )

    Department = models.CharField(
        "Departamento",
        max_length=64
    )

    Provice = models.CharField(
        "Provincia",
        max_length=64
    )

    District = models.CharField(
        "Distrito",
        max_length=64
    )

    class Meta:
        verbose_name = 'Madre'
        verbose_name_plural = 'Madres'

        db_table = TABLES['Mother']

    def __str__(self):
        fmt_data = {
            'firstName': 'Margery',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return 'Sra. {firstName:} {lastName:}'.format(**fmt_data)

    def __unicode__(self):
        fmt_data = {
            'firstName': 'Margery',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return u'Sra. {firstName:} {lastName:}'.format(**fmt_data)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Child object
class Child(models.Model):
    DNI = models.IntegerField(
        "Documento de identidad",
        unique=True
    )

    FirstName = models.CharField(
        "Nombre(s)",
        max_length=64,
    )

    LastName = models.CharField(
        "Apellido(s)",
        max_length=64,
    )

    BirthDate = models.DateField(
        "Fecha de nacimiento",
        default=date.today
    )

    Heigth = models.FloatField(
        "Estatura",
    )

    Weigth = models.FloatField(
        "Peso",
    )

    APGARRn = models.IntegerField(
        "APGAR Rn"
    )

    BirthPlace = models.CharField(
        "Lugar de Nacimiento",
        max_length=64,
    )

    Department = models.CharField(
        "Departamento",
        max_length=64
    )

    Provice = models.CharField(
        "Provincia",
        max_length=64
    )

    District = models.CharField(
        "Distrito",
        max_length=64
    )

    Mother = models.ForeignKey(
        Mother,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'

        db_table = TABLES['Child']

    def __str__(self):
        fmt_data = {
            'firstName': 'Margery',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return 'Niño(a) {firstName:} {lastName:}'.format(**fmt_data)

    def __unicode__(self):
        fmt_data = {
            'firstName': 'Margery',
            'lastName': 'Doe'
        }

        if self.FirstName:
            fmt_data.update({'firstName': self.FirstName})

        if self.LastName:
            fmt_data.update({'lastName': self.LastName})

        return u'Niño(a) {firstName:} {lastName:}'.format(**fmt_data)

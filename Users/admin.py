# -*- encoding: utf-8 -*-
from django.contrib import admin

from Users.models import Visitor
from Users.models import Mother
from Users.models import Child


class VisitorAdmin(admin.ModelAdmin):
    name = u'Visitador(a)'
    verbose_name = u'Visitadores(as)'

admin.site.register(Visitor, VisitorAdmin)


class MotherAdmin(admin.ModelAdmin):
    name = u'Madre'
    verbose_name = u'Madres'

admin.site.register(Mother, MotherAdmin)


class ChildAdmin(admin.ModelAdmin):
    name = u'Niño(a)'
    verbose_name = u'Niños(as)'

admin.site.register(Child, ChildAdmin)

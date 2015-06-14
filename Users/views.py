# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.db.models import Max
from django.db.models import Min
from django.template.context_processors import csrf

from Users.forms import LoginVisitorFrom
from Users.forms import MotherForm
from Users.models import Mother
# from Users.models import Visitor


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print username, type(username)
        print password, type(password)

        user = authenticate(username=username, password=password)
        print user

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('selector/')
            else:
                return HttpResponse('<h1>No way!</h1>')

        else:
            context = {}
            context.update(csrf(request))
            context = RequestContext(context)

            return render_to_response('login.html', {'loginForm': LoginVisitorFrom()}, RequestContext(request))

    form = LoginVisitorFrom()

    return render_to_response('login.html', {'loginForm': form}, RequestContext(request))


def selectorView(request):
    if not request.user.is_authenticated():
        return redirect('{0:}?next={1:}'.format('/', request.path))

    return render_to_response('selector.html', RequestContext(request))


class selectionView(TemplateView):
    template_name = 'birth.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('{0:}?next={1:}'.format('/', request.path))

        if kwargs['selection'] == 'parto':
            self.template_name = 'birth.html'

        elif kwargs['selection'] == 'control':
            self.template_name = 'control.html'

        elif kwargs['selection'] == 'contingencia':
            self.template_name = 'emergency.html'

        return super(selectionView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        dni = int(request.POST['dni'])

        if Mother.objects.filter(DNI=dni).exists():
            return HttpResponseRedirect('/selector/parto/registro/madre/?dni={0:}'.format(dni))
        else:
            return HttpResponse('<h1>No way!</h1>')

        args = [RequestContext(request)]

        return super(selectionView, self).get(request, *args, **kwargs)


class registroView(TemplateView):
    template_name = 'mother.html'

    def get(self, request, *args, **kwargs):
        if kwargs['register'] == 'madre':
            self.template_name = 'mother.html'
            if 'dni' in request.GET.keys():
                mother = Mother.objects.get(DNI=int(request.GET['dni']))
                form = MotherForm()

                kwargs.update({
                    'form': form,
                    'DNI': mother.DNI,
                    'FirstName': mother.FirstName,
                    'LastName': mother.LastName,
                    'BirthDate': mother.BirthDate,
                    'CivilState': mother.CivilState,
                    'Ocupation': mother.Ocupation,
                    'PreviousPregnancies': mother.PreviousPregnancies,
                    'Provice': mother.Provice,
                    'District': mother.District,
                })
        else:
            self.template_name = 'child.html'

        return super(registroView, self).get(request, *args, **kwargs)


class otherTemplates(TemplateView):
    template_name = ''

    def get(self, request, *args, **kwargs):
        return super(otherTemplates, self).get(request, *args, **kwargs)

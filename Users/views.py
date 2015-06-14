# -*- encoding: utf-8 -*-
from Users.forms import MedicFrom
from django.shortcuts import render_to_response


def registration(request):
    form = MedicFrom()

    return render_to_response("registro.html", {
        "form": form,
    })

"""ThAyllu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from Users.views import loginView
from Users.views import selectorView
from Users.views import selectionView
from Users.views import registroView
from Users.views import otherTemplates


urlpatterns = [
    url(r'^$', loginView, name='login'),
    url(r'^selector/$', selectorView, name='selector'),
    url(r'^selector/(?P<selection>(parto|control|contingencia))/$', selectionView.as_view(), name='selection'),
    url(r'^selector/parto/madre/$', selectorView, name='mother'),
    url(r'^selector/parto/registro/(?P<register>(madre|nino))/$', registroView.as_view(), name='register'),
    url(r'^selector/parto/registro/nino/vacunas/1/$', otherTemplates.as_view(template_name='cartillaVacuna1.html'), name='cartillaVacuna1'),
    url(r'^selector/parto/registro/nino/vacunas/2/$', otherTemplates.as_view(template_name='cartillaVacuna2.html'), name='cartillaVacuna2'),
    url(r'^selector/parto/registro/nino/vacunas/3/$', otherTemplates.as_view(template_name='cartillaVacuna3.html'), name='cartillaVacuna3'),
    url(r'^selector/parto/registro/nino/vacunas/4/$', otherTemplates.as_view(template_name='cartillaVacuna4.html'), name='cartillaVacuna4'),
    url(r'^selector/parto/registro/nino/vacunas/5/$', otherTemplates.as_view(template_name='cartillaVacuna5.html'), name='cartillaVacuna5'),
    url(r'^selector/parto/registro/nino/vacunas/6/$', otherTemplates.as_view(template_name='cartillaVacuna6.html'), name='cartillaVacuna6'),
    url(r'^selector/parto/registro/nino/vacunas/7/$', otherTemplates.as_view(template_name='cartillaVacuna7.html'), name='cartillaVacuna7'),
    url(r'^selector/parto/registro/nino/vacunas/8/$', otherTemplates.as_view(template_name='cartillaVacuna8.html'), name='cartillaVacuna8'),
    url(r'^selector/parto/registro/nino/vacunas/9/$', otherTemplates.as_view(template_name='cartillaVacuna9.html'), name='cartillaVacuna9'),
    url(r'^selector/recomendaciones/1/$', otherTemplates.as_view(template_name='recomendaciones1.html'), name='recomendaciones1'),
    url(r'^selector/recomendaciones/2/$', otherTemplates.as_view(template_name='recomendaciones2.html'), name='recomendaciones2'),
    url(r'^selector/recomendaciones/3/$', otherTemplates.as_view(template_name='recomendaciones3.html'), name='recomendaciones3'),
]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Page

who_we_are= Page.objects.filter(page_title='Who We Are')


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home-corporate.html', context=None)

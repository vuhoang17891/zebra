# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Page

def who_we_are():
    return Page.objects.filter(page_title='Who we are')

print '+++++++++++++++++++++++' + who_we_are() + '+++++++++++++++++++++++++++'

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home-corporate.html', context=None)

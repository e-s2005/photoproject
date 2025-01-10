from django.shortcuts import render
from django.views.generic import TemplateView
# from django.views.generic import DetailView

class IndexView(TemplateView):
    template_name = 'index.html'
    
# class Detailview(DetailView):
#     template_name='detail.html'
#     model = PhotoPost

from MyFeedapp.models import *
from django.views.generic import ListView
from MyFeedapp.views.jsonRequest_view import getData,converJsonDateToPython
from MyFeedapp.views.url_option_management import *


class HomePage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = General)
        jsonObjects = getData(url)
        jsonObjects=converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Home"
        context['Articles']=jsonObjects
        return context

class InternationalPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(language = Language_Eng)
        # import ipdb
        # ipdb.set_trace()
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "International"
        context['Articles']=jsonObjects
        return context


class SportsPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Sports)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Sports"
        context['Articles']=jsonObjects
        return context


class EntertainmentPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Entertainment)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Movies"
        context['Articles']=jsonObjects
        return context

class TechnologyPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Technology)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Technology"
        context['Articles']=jsonObjects
        return context

class SciencePage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Science)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Science"
        context['Articles']=jsonObjects
        return context

class HelthPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Health)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Helth"
        context['Articles']=jsonObjects
        return context

class BusinessPage(ListView):
    template_name = 'articles.html'
    login_url = '/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        url = get_url(country=country_india,category = Business)
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context = {}
        context['Title'] = "Business"
        context['Articles']=jsonObjects
        return context


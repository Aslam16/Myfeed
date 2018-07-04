from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from MyFeedapp.models import *
from django.views.generic import ListView
from MyFeedapp.views.jsonRequest_view import getData,converJsonDateToPython
from MyFeedapp.views.url_option_management import *

class SavedArticles(LoginRequiredMixin,ListView):
    template_name = 'user_saved_articles.html'
    login_url = '/v1/login/'
    context_object_name = 'Values'
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        # import ipdb
        # ipdb.set_trace()
        user = self.request.user
        Articles = Article.objects.filter(user=user)
        num_of_articles = len(Articles)
        if num_of_articles == 0:
            context['is_data_available'] = False
        else:
            context['is_data_available'] = True
        context['Title'] = "Saved Articles"
        context['Articles']=Articles
        return context
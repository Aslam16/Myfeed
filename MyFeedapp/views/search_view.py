from django.shortcuts import render

from MyFeedapp.models import *
from django.views.generic import ListView
from MyFeedapp.views.jsonRequest_view import getData,converJsonDateToPython
from MyFeedapp.views.url_option_management import *


def search(request):
    context = {}
    context['Title'] = ""
    context['Articles'] = None
    if request.method == "POST":
        # Get the posted form
        query= request.POST['search']
        url = search_url(query="q="+str(query))
        jsonObjects = getData(url)
        jsonObjects = converJsonDateToPython(jsonObjects)
        context['Title'] = query
        context['Articles'] = jsonObjects
    return render(request, 'basePageDisplay.html', context)
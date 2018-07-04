from django.contrib import admin
from django.urls import path
from MyFeedapp.views.webPages import *
from MyFeedapp.views.search_view import *
from MyFeedapp.views.save_view import *
from MyFeedapp.views.authentication_view import *
from MyFeedapp.views.user_web_page import *

urlpatterns = [
    path(r'',HomePage.as_view(),name='first_page'),
    path(r'home/',HomePage.as_view(),name='home_page'),
    path(r'sports/',SportsPage.as_view(),name='sports_page'),
    path(r'entertainment/',EntertainmentPage.as_view(),name='entertainment_page'),
    path(r'helth/', HomePage.as_view(), name='helth_page'),
    path(r'international/', InternationalPage.as_view(), name='international_page'),
    path(r'tech/', TechnologyPage.as_view(), name='tech_page'),
    path(r'science/', SciencePage.as_view(), name='science_page'),
    path(r'business/', BusinessPage.as_view(), name='business_page'),
    path(r'query/',search, name='search_page'),
    path(r'save/',save,name="save_page"),
    path(r'remove/',remove,name="remove_page"),
    path(r'signup/',signUp.as_view(),name="signup_page"),
    path(r'login/',loginUser.as_view(),name='login_page'),
    path(r'logout/',logout_view,name='logout_page'),
    path(r'saved/',SavedArticles.as_view(),name='user_saved_page'),
]

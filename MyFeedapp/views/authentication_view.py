from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from MyFeedapp.forms.signupForm import *
from MyFeedapp.models import *
from django.contrib.auth import logout,login

def logout_view(request):
    logout(request)

    return redirect(reverse_lazy('feed:home_page'))

class loginUser(View):
    def get(self,request):
        form = loginForm

        return render(
            request,
            template_name='signUpAndLogin.html',
            context={'form':form,'Title':"Login","link_to_next":"feed:signup_page","text_of_next":"Sign Up",'submit_text':"Log In"}
        )

    def post(self,request):
        form = loginForm(request.POST)

        if form.is_valid() :
            user = authenticate(
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect(reverse_lazy("feed:home_page"))
        else:
            return redirect(reverse_lazy('feed:login_page'))

class signUp(View):

    def get(self,request):

        form = signUpForm
        return render(
            request,
            template_name='signUpAndLogin.html',
            context={'form':form,'Title':"Sign Up","link_to_next":"feed:login_page","text_of_next":"Login",'submit_text':"Lets Start"}
        )

    def post(self,request):
        form = signUpForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is None:
                user = User.objects.create_user(
                    **form.cleaned_data
                )
                user.save()
                login(request, user)
                return redirect(reverse_lazy("feed:home_page"))
            return redirect(reverse_lazy("feed:signup_page"))
        # return render(
        #         request,
        #         template_name='collageBootstrap.html',
        #         context={'Headers':["ID","Name", "Acronym", "Email"],'Title': "Collage Details",'Values':Collage.objects.all()}
        #     )


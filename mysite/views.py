from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    """
        Provides the basic homapage for all those who are not logged in
    """
    return render_to_response('index.html')

def login(request):
    """
        Area for users to login
    """
    return render_to_response('login.html')

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
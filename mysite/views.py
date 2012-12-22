from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import login


def index(request):
    """
        Provides the basic homapage for all those who are not logged in
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect('/users/')
    else:
        return render_to_response('index.html')

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/users/')
    else:
        return login(request)
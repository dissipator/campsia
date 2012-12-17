from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from users.models import User
from django.contrib.auth.decorators import login_required



@login_required
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html',{'users':user})

@login_required
def index(request):
    current_user = request.user
    return render(request, 'users/dashboard.html',{'cuser':current_user})
    
@login_required
def attendance(request):
    current_user = request.user
    subjects = get_subjects(current_user)
    return render(request, 'users/attendance.html',{'subjects':subjects})

@login_required
def notifications(request):
    current_user = request.user
    notifications = get_notifications(current_user,5)
    return render(request, 'users/notifications.html',{'notifications':notifications})

@login_required
def dues(request):
    '''
    View for displaying all Dues and Bills
    
    Keyword Arguments:
    request -- request from browser
    
    Returns: render to a template
    '''
    current_user = request.user
    dues = get_dues(current_user)
    return render(request, 'users/dues.html',{'dues':dues})

@login_required
def inbox(request):
    current_user = request.user
    messages = get_messages(current_user)
    return render(request, 'users/inbox.html',{'messages':messages})
    
def get_subjects(user):
    '''
    Finds all the subjects taken by the user. 
    
    Keyword Arguments: 
    user -- user object
    
    Returns: List
    '''
    subjects = ['Engineering Mathematics','Discrete Computational Statistics','Computer Programming']
    return subjects

def get_notifications(user,number):
    '''
    Fetches required notifications for the user
    
    Keyword Arguments:
    user -- user object
    number -- integer ( maximum no of notifications required )
    
    
    Returns: List
    '''
    notifications = ['Sample Notification','Notification 2']
    return notifications

def get_dues(user):
    '''
    Fetches current dues fro the user
    
    Keyword Arguments:
    user -- user object
    
    Returns: List
    '''
    dues = ['Mess Bill','Library Fines','Tution Fees','Others']
    return dues

def get_messages(user):
    messages = [{'from':'Jezeel','subject':'hello','read':False},{'from':'Tony','subject':'hi','read':True}]
    return messages
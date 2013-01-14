# Create your views here.
from users.models import User
from rpc4django import rpcmethod


@rpcmethod(name='user.create', signature=['string','string','string','object'])
def remote_create_user(name,email,password):
    ''' 
    Creates a user from the RPC
    
    Keyword Arguments : 
    
    name -- username 
    email -- email address of user
    password -- password
    
    Returns : User
    '''
    
    user = User.objects.create_user(name,email,password)
    user.save()
    return user

    
@rpcmethod(name='hello.world', signature=['string'])
def rpctest():
    return "Hello World"


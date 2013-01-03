# Create your views here.
from users.models import User

#for RPC functions
from jsonrpc import jsonrpc_method

@jsonrpc_method('user.create')
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

    
@jsonrpc_method('rpc.test')
def rpctest():
    return "Hello World"


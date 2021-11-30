from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                
                if(request.user.groups.filter(name__in=allowed_roles).exists()):
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Sorry you are not de developer of this plataform')
            else:
                return HttpResponse('Sorry you are not de developer of this plataform(Has no group)')
        return wrapper_func
    return decorator
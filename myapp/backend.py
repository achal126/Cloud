
from .models import Login
from django.shortcuts import Http404

class MyBackEnd(object):
    """
    This is the custom backend to authenticate the user in the DB.
    if this authentication fais then django default authentication  will get called
    """

    def authenticate(self, email, password):
        user = Login.objects.get(username= email)
        user_name=get_user(email)

        if email == user_name:
            a=1
        else:
            return Http404



def get_user(self, email):
    try:
        return Login.objects.get(username=email)
    except email.DoesNotExist:
        return None
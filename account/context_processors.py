from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def check_superuser_status(request):
    current_user = request.user
    context = {
        'current_user': current_user
    }
    return context


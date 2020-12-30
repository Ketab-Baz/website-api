from django.http import JsonResponse
from .models import User, Critic
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account_type = request.POST['account_type']
        if account_type == 'user':
            user_login(request, username, password)
        elif account_type == 'critic':
            critic_login(request, username, password)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        birthday = request.POST['birthday']
        account_type = request.POST['account_type']
        if account_type == 'user':
            user_register(username, password, email, phone_number, birthday)
        elif account_type == 'critic':
            critic_register(username, password, email, phone_number, birthday)


def user_register(username, password, email, phone_number, birthday):
    user = User.objects.filter(username=username) | User.objects.filter(
        phone_number=phone_number) | User.objects.filter(email=email)
    if user is not None:
        response = {
            'response': 'success',
            'message': 'Register Successful'
        }
        User(username=username, password=password, email=email, phone_number=phone_number, birthday=birthday).save()
        return JsonResponse(response, status=200)
    else:
        response = {
            'response': 'failed',
            'message': 'username or phone number or email is registered before'
        }
        return JsonResponse(response, status=400)


def critic_register(username, password, email, phone_number, birthday):
    user = Critic.objects.filter(username=username) | Critic.objects.filter(
        phone_number=phone_number) | Critic.objects.filter(email=email)
    if user is not None:
        response = {
            'response': 'success',
            'message': 'Register Successful'
        }
        Critic(username=username, password=password, email=email, phone_number=phone_number, birthday=birthday).save()
        return JsonResponse(response, status=200)
    else:
        response = {
            'response': 'failed',
            'message': 'username or phone number or email is registered before'
        }
        return JsonResponse(response, status=400)


def user_login(request, username, password):
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            auth.login(request, user)
            response = {
                'response': 'success',
                'message': 'Login Successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'response': 'failed',
                'message': 'username or password is incorrect'
            }
            return JsonResponse(response, status=401)
    except User.DoesNotExist:
        response = {
            'response': 'failed',
            'message': 'username or password is incorrect'
        }
        return JsonResponse(response, status=401)


def critic_login(request, username, password):
    try:
        user = Critic.objects.get(username=username)
        if user.password == password:
            auth.login(request, user)
            response = {
                'response': 'success',
                'message': 'Login Successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'response': 'failed',
                'message': 'username or password is incorrect'
            }
            return JsonResponse(response, status=401)
    except Critic.DoesNotExist:
        response = {
            'response': 'failed',
            'message': 'username or password is incorrect'
        }
        return JsonResponse(response, status=401)

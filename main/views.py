from django.http import JsonResponse
from django.shortcuts import render
import json

from .models import Subscription

# Create your views here.
def subscription(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        try:
            sub = Subscription.objects.get(user_email = user_email)
            sub.user_name = user_name
        except:
            sub = Subscription.objects.create(user_email = user_email, user_name = user_name)
        sub.save()
        return JsonResponse({'message': 'Данные пользователя сохранены'})
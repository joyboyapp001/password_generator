from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    # return HttpResponse('<h1>hello django!</h1>')
    return render(request, './index.html')


def password(request):
    length = eval(request.GET.get('length'))
    input_length = request.GET.get('input-length')

    password_char = 'abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('uppercase') == 'on':
        password_char += password_char.upper()

    if request.GET.get('number') is not None:
        password_char += '0123456789'

    if request.GET.get('special'):
        password_char += "!@#$%^&*?"

    if input_length != '':
        length = eval(input_length)

    password = ''.join([random.choice(password_char) for i in range(length)])

    print(length, password, password_char)
    return render(request, './password.html', {'password': 'abcde'})

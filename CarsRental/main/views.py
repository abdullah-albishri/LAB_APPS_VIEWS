from django.shortcuts import render
from django.http import HttpResponse , HttpRequest, JsonResponse
import secrets
import string
import json

# Create your views here.

def home(request: HttpRequest):
    return render(request , "main/home.html")

def about_view(request: HttpRequest):
    return render(request , "main/about.html")

def password(request: HttpRequest):
    random_password = generate_secure_random_string(10)
    return HttpResponse(random_password)

def generate_secure_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_random_string = ''.join(secrets.choice(characters) for i in range(length))
    return secure_random_string
def get_json(request: HttpRequest):
    # return jason response with data from data.json file
    with open("main/data.json", "r") as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
    

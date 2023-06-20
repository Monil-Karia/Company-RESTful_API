'''
Functions based and class based views
'''
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def home_page(request):
    print("Home Page Requested")
    friends = [
        'ankit','ravi','uttam'
    ]
    # return HttpResponse("This is Home page") #We can send JSON in the response of the function\
    return JsonResponse(friends,safe=False)
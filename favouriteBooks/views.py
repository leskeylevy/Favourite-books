from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    """
    Function to render homepage    
    """
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    return HttpResponse(content=f'Hello World the time in Niarobi now is {timenow}')
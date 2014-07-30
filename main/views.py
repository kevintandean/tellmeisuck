# from django.core.serializers import json
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from main.forms import PostForm


def login(request):
    form = PostForm()
    data = {'postform':form}
    return render(request,'login.html', data)

@csrf_exempt
def display_friends(request):
    if request.method == 'POST':
        print "yeay"
        data = json.loads(request.body)['data']
        print data

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
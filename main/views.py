# from django.core.serializers import json
from django.shortcuts import render, render_to_response
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from main.forms import PostForm
from main.models import UserProfile


def login(request):
    form = PostForm()
    data = {'postform':form}
    return render(request,'login.html', data)

# @csrf_exempt
def display_friends(request):
    if request.method == 'POST':
        data = json.loads(request.body)['data']
        print data
        return render(request,'friends.html',{'data':data})

# @csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        UserProfile.objects.get_or_create(first_name=data['first_name'], last_name=data['last_name'], user_id=data['user_id'], email=data['email'], new='true')
        print data

def post(request):
    if request.method=='POST':
        print json.loads(request.body)

    else:
        form = PostForm()

    return render(request,'form.html',{'form':form})



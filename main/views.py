# from django.core.serializers import json
from django.shortcuts import render, render_to_response
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from main.forms import PostForm
from main.models import UserProfile, Post

def check_new_post(request, user_id, post_id):
    user = UserProfile.objects.get(user_id=user_id)
    posts = Post.objects.filter(id__gt=post_id, recipient=user).order_by('-id')
    print posts
    if len(posts)==0:
        # This should probably return an empty string at least?
        return
    else:
        return render(request,'new_post.html', {'posts':posts})


# Should be using Django's built in Auth functionality, guessing it wasn't working well with your custom UserProfile model
def login(request):
    form = PostForm()
    data = {'hidden':'none'}
    return render(request,'login.html', data)

def login_redirect(request, user_id):
    user = UserProfile.objects.get(user_id=user_id)
    data = {'hidden': user_id, 'name':user.first_name+ ' ' +user.last_name}
    return render(request, 'login.html', data)

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
        # use string.format() here instead of adding strings
        data['name']=data['first_name']+ ' ' + data['last_name']
        return render(request, 'me.html', {'data':data})

def post(request):
    # Why not use the PostForm to save if you're passing it to the template to display
    if request.method=='POST':
        data = json.loads(request.body)
        author = UserProfile.objects.get(user_id=data['author'])
        print author
        recipient = UserProfile.objects.get(user_id=data['recipient'])
        # print recipient
        Post.objects.create(author=author, recipient=recipient, good=data['good'], bad = data['bad'])
        print "yeay"

    else:
        form = PostForm()

    return render(request,'form.html',{'form':form})

def get_post(request, user_id):
    user = UserProfile.objects.get(user_id=user_id)
    posts = Post.objects.filter(recipient=user).order_by('-created')
    first_name = user.first_name
    last_name = user.last_name
    return render(request,'display_post.html', {'posts':posts, 'first_name':first_name, 'last_name':last_name, 'user_id':user_id})

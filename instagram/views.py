from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .feedform import CreateFeed
from .models import Feeds
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'Userpage/homepage.html')


def signuppage(request):
    if request.method == 'GET':
        return render(request, 'Userpage/signuppage.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                            first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'], email=request.POST['email'],
                                            password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('postfeed')

def loginpage(request):
    if request.method == 'GET':
        return render(request, 'Userpage/loginpage.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Userpage/loginpage.html', {'error':'Wrong User details'})
        else:
            login(request, user)
            return redirect('postfeed')

def logoutpage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginpage')

#After authentication
@login_required
def postfeed(request):
    user = request.user
    feeds = Feeds.objects.filter(user=request.user,)

    return render(request, 'Posts/feed.html', {'user':user, 'feeds':feeds})

@login_required
def createfeed(request):
    if request.method == 'GET':
        return render(request, 'Posts/createfeed.html', {'form':CreateFeed})
    else:
        try:
            data = {
                'feedtitle' : request.POST['feedTitle'],
                'imgFeeed' : request.FILES.get('imgFeed'),
                'caption' : request.POST['caption']
            }

            form = CreateFeed(request.POST,request.FILES)
            print(data)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('postfeed')
        except ValueError:
            return render(request, 'Posts/createfeed.html',
                          {'form': CreateFeed(), 'error': 'Bad data passed in. Try again.'})
@login_required
def profilepage(request):
    user = request.user
    feeds = Feeds.objects.filter(user=request.user,)

    return render(request, 'Posts/profile.html', {'user': user, 'feeds':feeds})
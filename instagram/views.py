from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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
            return redirect('postpage')

def loginpage(request):
    if request.method == 'GET':
        return render(request, 'Userpage/loginpage.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Userpage/loginpage.html', {'error':'Wrong User details'})
        else:
            login(request, user)
            return redirect('postpage')


#After authentication
def postpage(request):
    user = request.user
    return render(request, 'Posts/post.html', {'user':user})
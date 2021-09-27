from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from myapp.models import signup
from django.core.files.storage import FileSystemStorage
# Create your views here.


def contact(request):
    return render(request, 'contact.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'upload.html', context)


def signup(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                return redirect('signup')
            elif User.objects.filter(username=Username).exists():
                messages.info(request, 'Username already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=Username, email=email, password=password)
                user.save();
                messages.info(request, "Signup successful")
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):

    return render(request, 'login.html')

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import request
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm, BookForm, DocumentForm
from .models import Seller, Book, Document
# Create your views here.


def index(request):
    doc = Document.objects.get(id=1)
    return render(request, 'index.html',{'doc':doc})
    # return HttpResponse(content=request.user.seller.school)


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            sel = Seller.objects.create(
                school=form.cleaned_data['School'],
                phone=form.cleaned_data['Phone'], user_id=user.id)
            login(request, user)
            return HttpResponse(content=form.cleaned_data)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def Userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse(content="You are logged in successfully")
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # if user:
            #     login(request, user)
            # else:
            #     err = "incorrect username or password"
            #     form = LoginForm()
            # return render(request, 'login.html',
            #                   {'error': err, 'form': form})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def BookCreateOrUpdate(request, id):
    instance = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('Home:index')
    return render(request, 'book.html', {'form': form})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home:index')
    else:
        form = DocumentForm()
    return render(request, 'form_upload.html', {
        'form': form
    })

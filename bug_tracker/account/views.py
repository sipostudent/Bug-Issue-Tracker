from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django import forms
import django.db

from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import User


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                assert(user.password == password)
            except AssertionError:
                form.add_error('password', 'Incorrect password.')
            except ObjectDoesNotExist:
                form.add_error('email', 'No account registered to this email.')
            else:
                request.session['user_email'] = email
                return redirect('/')

    return render(request, 'login.html', {'form': form})

def logout(request):
    request.session['user_email'] = ''

    return redirect('/')


def profile(request):
    email = request.session.get('user_email')
    
    if email:
        try:
            user = User.objects.get(email=email)
            name = user.name
            email = user.email
            notes = user.notes
        except ObjectDoesNotExist:
            return redirect('login')
        else:
            return render(request, 'profile.html', {'name': name, 'email': email, 'notes': notes})

    return redirect('login')


def edit_profile(request):
    email = request.session.get('user_email')
    
    if email:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return redirect('login')
        else:
            form = EditProfileForm(initial={
                'name': user.name,
                'email': user.email,
                'notes': user.notes
            })

            if request.method == 'POST':
                form = EditProfileForm(request.POST)

                if form.is_valid():
                    print("Form validatied")
                    user.name = form.cleaned_data['name']
                    user.email = form.cleaned_data['email']
                    user.notes = form.cleaned_data['notes'] or ''
                    
                    try:
                        user.save()
                        print("User saved")
                    except django.db.IntegrityError:
                        form.add_error('email', 'This email already exists.')
                else:
                    print("Invalid form")

            return render(request, 'edit_profile.html', {'form': form})

    return redirect('login')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User(name=name, email=email, password=password)
                user.save()
            except django.db.IntegrityError:
                form.add_error('email', 'This email already exists.')
            else:
                return render(request, 'login.html')

    return render(request, 'register.html', {'form': form})

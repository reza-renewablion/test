from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from users.forms import SignUpForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


# def user_login(request):
#     next_path = None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=cd['username'],
#                 password=cd['password']
#             )
#             if user and user.is_active
#     else:
#         form = LoginForm()
#         if request.method == 'GET':
#             next_path = request.GET.get('next')
#
#     return render(request, 'users/login.html', {'form': form, 'next': next_path})

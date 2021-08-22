from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm, Register_Form

User = get_user_model()


def register_view(request):
    form = Register_Form(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password2= form.cleaned_data.get('password2')

        try:
            user = User.objects.create_user(username, email, password)
            print(user)

        except:
            user = None
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['register_error'] = 1
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)

@login_required()
def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['register_error'] = 1
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.

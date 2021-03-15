from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm




def registerPage(request):
    form = CreateUserForm()
    #перемменая для ошибки
    error = ''
    # Отслеживать добавление данных в БД
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            #отправляем сообщение что все хорошо и пользователь зарегистрирован
            messages.success(request, 'Account was created for' + ' ' + user)
            # переадресация на страницу с тасками
            return redirect('login')
        # если форма не кореектная то ошибку выбивать будет
        else:
            error = 'error'


    context = {
        'form': form,
        'error': error
    }
    return render(request, 'users/registerpage.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/loginpage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



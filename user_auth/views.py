from django.contrib import messages
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from user_auth.models import DeliveryUser
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
# User login
def user_login(request):
    if request.method == 'POST':
        email_address = request.POST.get('user_email')
        row_password = request.POST.get('user_pwd')
        logging_user = authenticate(request, email=email_address, password=row_password)
        if logging_user is not None:
            # request.session.set_expiry(3600)
            login(request, logging_user)
            return redirect('routes_path')
        else:
            messages.error(request, 'Email or password is incorrect')

    return render(request, 'user_auth/user_login.html')

# User logout
def user_logout(request):
    request.session.flush()
    logout(request)
    return redirect('login_path')

# User registration
def user_registration(request):
    if request.method == "POST":
        firstname = request.POST.get('reg_form_firstname_input')
        lastname = request.POST.get('reg_page_lastname_input')
        user_mail = request.POST.get('reg_form_email_input')
        user_pwd = request.POST.get('reg_form_password_input')

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$'

        if re.match(password_regex, user_pwd):
            new_user = User(
                firstname=firstname,
                lastname=lastname,
                email=user_mail,
                password=make_password(user_pwd),
                is_active=False

            )
            new_user.save()
            messages.success(request,
                             'Your account has been created successfully! You will be able to login once it is '
                             'approved')
        else:
            messages.error(request, 'Password must contain at least one uppercase letter, one lowercase letter, '
                                    'one digit, and one special character.')

        # return redirect('login_path')

    return render(request, 'user_auth/user_registration.html')


@login_required(login_url='login_path')
def landing_dashboard(request):
    return render(request, 'dashboards/landing_dashboard.html')

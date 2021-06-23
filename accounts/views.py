from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password,password_validators_help_texts
def register(request):

    context ={
        "pass" : password_validators_help_texts()
    }
    if request.method == 'POST':
        # Register user

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:

            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use')
                return redirect('register')
            else:
                # Check email
                
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email address already in use')
                    return redirect('register')
                else:

                    validate = None

                    try:
                       validate = validate_password(password=password2)
                    except Exception as e:
                        validate = 0
                        msg =  str(e).replace(']', '')
                        msg =  msg.replace('[', '')
                        messages.error(request,msg)
                        
                    print(validate)
                    if validate is not None:
                        return redirect('register')
                    else:    
                    
                        # Successful Registration
                        user = User.objects.create_user(
                            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                        # Redirect to login page after register
                        user.save()
                        messages.success(
                            request, 'You are now registered and can log in')
                        return redirect('login')

                    # Login after Register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)
def login(request):
    if request.method == 'POST':
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username and password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):

    auth.logout(request)
    messages.success(request, "You are now logged out")

    return redirect('index')
    
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

        
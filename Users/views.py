from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Users.forms import CustomUserCreationForm

# username - Aman
# password - aman


# python -m smtpd -n -c DebuggingServer localhost:1025
# type the above in terminal to start local smtp server
def dashboard(request):
    return render(request, 'Users/dashboard.html')

def register(request):
    if request.method == 'GET':
        return render(
            request, 'Users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # This creates an User, but it's not immediately saved
            user.backend = 'django.contrib.auth.backends.ModelBackend'   # This associates a github backend to the above line 24 User, and thn saves it to the database
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))

# Here’s a breakdown of the register() view:
#
# Lines 17 to 21: If the view is displayed by a browser, then it will be accessed by a GET method.
#                 In that case, a template called users/register.html will be rendered.
#                 The last argument of .render() is a context, which in this case contains your custom user creation form.
#
# Lines 22 to 23: If the form is submitted, then the view will be accessed by a POST method.
#                 In that case, Django will attempt to create a user.
#                 A new CustomUserCreationForm is created using the values submitted to the form, which are contained in the request.POST object.
#
# Lines 24 to 27: If the form is valid, then a new user is created on line 25 using form.save().
#                 Then the user is logged in on line 27 using login().
#                 Finally, line 28 redirects the user to the dashboard.
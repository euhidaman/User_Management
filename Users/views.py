from django.shortcuts import render

# username - Aman
# password - password

# https://realpython.com/django-user-management/#change-passwords

# Create your views here.
def dashboard(request):
    return render(request, 'Users/dashboard.html')
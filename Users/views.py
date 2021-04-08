from django.shortcuts import render

# username - Aman
# password - password

# Create your views here.
def dashboard(request):
    return render(request, 'Users/dashboard.html')
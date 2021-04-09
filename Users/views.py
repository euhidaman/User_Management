from django.shortcuts import render

# username - Aman
# password - aman

# python -m smtpd -n -c DebuggingServer localhost:1025
# type d above in terminal to start local smtp server
def dashboard(request):
    return render(request, 'Users/dashboard.html')
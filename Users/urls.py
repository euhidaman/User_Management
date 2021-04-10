from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
    # the above will open up path to login, logout and basically everything which has a template in 'registration'
    path('register/', views.register, name='register'),
    path('oauth/', include('social_django.urls')),  # This line is to use Social Auth like GitHub , gmail login
]

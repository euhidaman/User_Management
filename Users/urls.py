from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
]
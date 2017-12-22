"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views as myapp_view

urlpatterns = [
    path(r'', myapp_view.index),
    path('admin/', admin.site.urls),
    path('index/', myapp_view.index),
    path('login_action/', myapp_view.login_action),
    path('event_manage/', myapp_view.event_manage),
    path(r'accounts/login/$', myapp_view.index),
]

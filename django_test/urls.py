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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from myapp import views as myapp_view

urlpatterns = [
    url(r'^$', myapp_view.index),
    path('admin/', admin.site.urls),
    url(r'^index/$', myapp_view.index),
    url(r'^login_action/$', myapp_view.login_action),
    url(r'^event_manage/$', myapp_view.event_manage),
    url(r'^accounts/login/$', myapp_view.index),
    url(r'^search_name/$', myapp_view.search_name),
    url(r'^guest_manage/$', myapp_view.guest_manage),
    url(r'^search_realname/$', myapp_view.search_realname),
    url(r'^sign_index/(?P<eid>[0-9]+)/$', myapp_view.sign_index),
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', myapp_view.sign_index_action),
    url(r'^logout/$', myapp_view.logout),
    url(r'^api/', include('sign.urls', namespace='sign')),
]

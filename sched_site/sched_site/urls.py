"""sched_site URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from res_sched import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.profile_view, name="profile"),
    url(r'^files/$', views.file_view, name="files"),
    url(r'^schedule/$', views.schedule_view, name="schedule"),
    url(r'', views.home, name="home"),
]

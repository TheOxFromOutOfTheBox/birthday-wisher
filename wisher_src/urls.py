"""wisher_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from pages.views import CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password/change/',CustomPasswordChangeView.as_view(),name='account_change_password'),
    path('accounts/', include('allauth.urls')),
    path('',include('pages.urls',namespace='pages')),
    path('wisher/',include('wish.urls',namespace='wish')),
]

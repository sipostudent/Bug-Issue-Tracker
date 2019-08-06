"""issue_tracker URL Configuration

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
from django.urls import path, include

# TODO: Include the paths from the account application.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Format is path function, the path as a string, then the include function, and an import path.
    # import path is app name and the urls file.
    path('', include('issue_tracker.urls')),
    path('account/', include('account.urls')),
    path('donations/', include('donations.urls')),
]

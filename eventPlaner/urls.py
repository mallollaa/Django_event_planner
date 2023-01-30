"""eventPlaner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
#this will be temproray .. delate it after creating the views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from users import views as users_views
from events import views as events_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', TemplateView.as_view(template_name = "base.html"),name='base'),
    path('home/', TemplateView.as_view(template_name = "home.html"),name='home'),
    path('register/', users_views.register_user, name='register'),
    path('login',users_views.login_view, name='login'),
    path('logout',users_views.logout_view, name='logout'),
    path('events_list', events_views.get_events, name='events'),
    # path('event', events_views.events_area, name='event'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
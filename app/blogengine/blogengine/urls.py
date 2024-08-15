"""
URL configuration for blogengine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from .views import redirect_blog

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls')),
    path('rest/', include('RestApi.urls')),
    path('qrf/', include('quick_start.urls')),
    path('movie/', include('django_movie.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('contacts/',include('contact.urls')),
    path('i18n/',include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('pages/',include('django.contrib.flatpages.urls')),
    path('contact/',include('contact.urls')),
    path("", include('django_movie.urls'))
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




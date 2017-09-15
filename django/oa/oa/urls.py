"""oa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from loaddata import views as loaddataView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^list/',  article.views.list, name='list'),
    # url(r'^index/', 'article.views.index', name='index'),
    # url(r'^detail/', 'article.views.detail', name='detail'),
    # url(r'^add/', 'article.views.add', name='detail'),
    # url(r'^do_add/', 'article.views.doAdd', name='detail'),
    url(r'^loaddata/', loaddataView.index, name='loaddata'),
]

urlpatterns += static('/media/', document_root='media')

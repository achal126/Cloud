"""Cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import TemplateView

from django.conf.urls.static import static
import settings
from myapp.views import achal1, login
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^connection/',TemplateView.as_view(template_name = 'User.html')),
    url(r'^achal1/', achal1, name= 'achal1'),
    url(r'^login/', login, name='login'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
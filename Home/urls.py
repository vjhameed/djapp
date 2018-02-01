from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.views.generic import CreateView
from .models import Book

app_name = 'Home'
urlpatterns = [
    url(r'home$', views.index, name='index'),
    url(r'contact$', views.contact, name='contact'),
    url(r'signup$', views.signup, name='signup'),
    url(r'login$', views.Userlogin, name='login'),
    url(r'book/(?P<id>\d+)$', views.BookCreateOrUpdate, name='book'),
    url(r'form$', views.model_form_upload, name='bok'),
    url(r'form$', views.model_form_upload, name='bok'),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

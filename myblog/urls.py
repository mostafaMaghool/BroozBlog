from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about , name='about'),
    path('', views.home , name='home'),
    path('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
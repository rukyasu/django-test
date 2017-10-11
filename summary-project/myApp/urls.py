from django.conf.urls import url
from myApp import views

app_name = 'myApp'

urlpatterns = [
    url(r'^players/$', views.players, name='players'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    ]

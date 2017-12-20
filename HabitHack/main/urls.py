from django.conf.urls import url
from django.urls import reverse_lazy, path
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^welcome/$', views.index, name = 'index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('main:index')), name='logout'),
    url(r'^register/$', views.register, name='register'),
    path('user/<username>/', views.user_profile, name='user'),
    path('settings/', views.edit_user_profile, name='edit_user'),
    path('home/', views.home, name='home'),
]

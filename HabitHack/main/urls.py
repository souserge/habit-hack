from django.conf.urls import url
from django.urls import reverse_lazy, path
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)
from . import views



app_name = 'main'
urlpatterns = [
    #url(r'^index/', views.index),
    #url(r'^$', views.index),

    url(r'^$', views.index, name = 'index'),
    #url(r'^index/$', views.HomePage.as_view(), name = 'index'),
    url(r'^index/$', views.index, name = 'index'),

    #url(r'^login/$', LoginView.as_view(template_name='main/login_test.html'), name='login'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('main:login')), name='logout'),

    url(r'^register/$', views.register, name='register'),
    # url(r'^profile/$', views.profile, name='profile'),
    path('user/<username>/', views.profile, name='user'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

]

from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)
from . import views


app_name = 'main'
urlpatterns = [
    #url(r'^index/', views.index),
    #url(r'^$', views.index),

    url(r'^$', views.HomePage.as_view(), name = 'index'),
    url(r'^index/$', views.HomePage.as_view(), name = 'index'),

    url(r'^login/$', LoginView.as_view(template_name='main/login_form.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('main:login')), name='logout'),

    url(r'^signup/$', views.signup, name='signup'),

]

from .import views
from django.urls import path, include
app_name = 'main'

urlpatterns = {
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('donate.html', views.donate, name='donate'),
    path('LoginRegister.html', views.LoginRegister, name='LoginRegister'),
    path('AdminLogin.html', views.AdminLogin, name='AdminLogin'),

}

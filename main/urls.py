from .import views
from django.urls import path, include
app_name = 'main'

urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('donate/', views.donate, name='donate'),
    path('', views.LoginRegister, name='LoginRegister'),
    path('user/adminlogin/', views.loginadmin, name='AdminLogin'),
    path('logout/', views.logout, name='logout'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),
    path('update/<int:c_id>', views.update, name="update"),
    path('delete/<int:c_id>', views.delete, name="delete"),
    path('user/dashboard/', views.userdashboard),
    path('useredit/', views.useredit),
    path('userupdate/<int:c_id>', views.userupdate)
]

from .import views
from django.urls import path, include
app_name = 'main'

urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('donate/', views.donate, name='donate'),
    path('', views.LoginRegister, name='LoginRegister'),
    path('admin/login/', views.AdminLogin, name='AdminLogin'),
    path('logout/', views.logout, name='logout'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),
    path('update/<int:c_id>', views.update, name="update"),

]

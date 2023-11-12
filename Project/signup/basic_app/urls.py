from django.urls import path
from basic_app import views

app_name = 'basic_app'
urlpatterns = [   
    path('user_login', views.loginPage ,name='user_login'),
    path('', views.registerPage ,name='user_register'),
    path('user_logout', views.logoutUser ,name='user_logout'),
    path('successful_login/', views.successfulLogin ,name='successful_login'),
]

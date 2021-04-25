from django.urls import path
from .views import LoginView, RegisterView, logout_user

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout')
]
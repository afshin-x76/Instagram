from django.urls import path
from .views import LoginView, RegisterView, logout_user, UsersListView, UserDetailView, FollowView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('list/', UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('follow/<int:pk>/', FollowView.as_view(), name='follow')
]
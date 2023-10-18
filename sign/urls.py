from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, LoginView, LogoutView

app_name = 'sign'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup')
]

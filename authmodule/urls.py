from django.urls import path
from authmodule.views import RegistrationView, PasswordUpdateView, UpdateProfileView, UserLoginView, UserDeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register',RegistrationView.as_view(),name = 'register'),
    path('login',UserLoginView.as_view(),name = 'login'),
    path('logout',LogoutView.as_view(),name = 'logout'),
    path('user/<int:pk>',login_required(UpdateProfileView.as_view()),name = 'profile'),
    path('changepassword/<int:pk>', login_required(PasswordUpdateView.as_view()), name='changepassword'),
    path('deleteaccount/<int:pk>', login_required(UserDeleteView.as_view()), name='deleteaccount'),
]

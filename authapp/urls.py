from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView
from django.urls import path, include

from .views import UserProfileView

urlpatterns = [
    # path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('reset/', PasswordResetView.as_view(), name="rest_password_reset"),

    path("user/", UserProfileView.as_view(), name="rest_user_details"),

]
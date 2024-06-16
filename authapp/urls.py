from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView
from django.urls import path, include


urlpatterns = [
    # path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('reset/', PasswordResetView.as_view(), name="rest_password_reset"),

]
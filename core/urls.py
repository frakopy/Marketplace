from django.urls import path, include
from .views import (
    index,
    about,
    contact,
    privacy,
    term_of_use,
    signup_view,
    CustomLoginView,
    CustomLogoutView,
    email_exist_with_us,
)

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("privacy/", privacy, name="privacy"),
    path("term/", term_of_use, name="term"),
    path("signup/", signup_view, name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    # Paths for Google authentication
    path("accounts/social/signup/", email_exist_with_us, name="email_exist_with_us"),
    path("accounts/", include("allauth.urls")),
]

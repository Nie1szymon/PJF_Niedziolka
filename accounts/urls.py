from django.urls import path

from .views import SignUpView, users_view


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("listofuser/", users_view, name="listofuser"),
]

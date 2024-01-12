from django.urls import path

from .views import SignUpView, users_view, change_group


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("listofuser/", users_view, name="listofuser"),
    path('change_group/<int:user_id>/', change_group, name='change-group'),
]

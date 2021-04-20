from django.urls import path

from .views import SigninView, SignoutView, SignupView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("signin/", SigninView.as_view()),
    path("signout/", SignoutView.as_view()),
]

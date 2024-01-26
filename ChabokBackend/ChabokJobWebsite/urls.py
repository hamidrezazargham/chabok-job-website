from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("home/", views.home_page, name="home"),
    path("jobs/<str:pk>/", views.view_job, name="viewjob"),
]
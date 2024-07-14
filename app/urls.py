from django.urls import path
from .import views

urlpatterns = [
    path("", views.HomePage.as_view(),name="homepage"),
    path("recurments", views.RecurmentPage.as_view(),name="recurments"),
    path("services", views.ServicePage.as_view(),name="services"),
    path("search", views.SearchPage.as_view(),name="search"),
    path("companies", views.CompanyPage.as_view(),name="companies"),
    path("login", views.LoginPage.as_view(),name="login"),
    path("signup", views.SignupPage.as_view(),name="signup"),
    path("logout", views.LogoutPage.as_view(),name="logout"),
]

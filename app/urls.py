from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='apps'),
    path('signup', views.handleSignUp, name='handleSignUp'),
    path('login', views.handeLogin, name='handleLogin'),
    path('logout', views.handelLogout, name='handleLogout'),
    path("login", views.login, name='login'),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("checkout/", views.checkout, name="Checkout"),
    path("products/<int:myid>", views.productView, name="productView"),
    path('search', views.search, name='search'),


]

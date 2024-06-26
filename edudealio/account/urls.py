from django.urls import path, include
from app.views import ErrorView
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # login register logout
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterUser.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),

]

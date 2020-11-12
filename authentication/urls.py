from django.urls import path
from authentication.views import Login, Register, Logout

urlpatterns = [
    path('login/', Login, name="login_user"),
    path('logout/', Logout, name="logout"),
    path('register/', Register, name="register_user"),
]

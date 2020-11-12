from django.urls import path, include
from .views import Login, Registration

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
]
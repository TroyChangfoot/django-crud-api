from django.urls import path
from .views import RegisterView, AccountView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("user/", AccountView.as_view(), name="user"), 
]

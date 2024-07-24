from django.urls import path, re_path
from api.viewset.AuthViewset import LoginViewset

app_name = "api"
urlpatterns = [
  path("login/", LoginViewset.as_view({ 'post': 'post' }), name="login_api"),
]
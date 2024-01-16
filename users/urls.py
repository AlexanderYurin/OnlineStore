from django.conf.urls.static import static
from django.urls import path

from app.settings import MEDIA_URL, MEDIA_ROOT
from users.views import RegistrationUser, ProfileView, LogoutUser, LoginUser


app_name = "users"


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("registration/", RegistrationUser.as_view(), name="registration"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutUser.as_view(), name="logout"),

]
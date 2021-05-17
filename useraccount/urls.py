from django.urls import path
from useraccount.views import login_view,signup_view,send_confirm_email,create_profile,profile_list,edit_profile,delete_profile,logout_view
# from useracccount.views import UserLogin

app_name = "user"

urlpatterns = [

    path("login/",login_view,name="login"),
    # path("login/", UserLogin.as_view(), name="login"),
    path("logout/",logout_view, name= "logout"),
    path("register/",signup_view,name="register"),
    path("send-email/",send_confirm_email,name="send_mail"),
    path("user-list/",profile_list,name="user_list"),
    path("user-profile/",create_profile,name="profile"),
    path("profile-edit/<int:id>/",edit_profile,name="user_edit"),
    path("profile-delete/<int:id>/",delete_profile,name="user_delete"),

]
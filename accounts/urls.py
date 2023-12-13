from django.urls import path
from .views import UserRegistrationView, EditProfileView,PasswordChangeFormView,UserProfileView,EditProfilePageView,CreateUserProfile
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/', PasswordChangeFormView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_success/', views.password_success,name='password_success'),
    path('<int:pk>/profile/', UserProfileView.as_view(),name='user_profile_view'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),name='edit_profile_page'),
    path('Create_User_Profile/', CreateUserProfile.as_view(),name='Create_User_Profile'),

]
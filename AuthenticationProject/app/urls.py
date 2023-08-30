from django.urls import path
from . import views
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import CustomAuthenticationForm,CustomPasswordResetForm,CustomPasswordSetForm

urlpatterns = [
    path('',views.home,name="home"),
]

################# register,login,logout #####################################
urlpatterns +=[
    path('register/',views.register,name='register'),
    path('accounts/login/',LoginView.as_view(form_class=CustomAuthenticationForm),name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
]

################################## for Forgot password urls ###########################
urlpatterns +=[
    path('accounts/password_reset/',PasswordResetView.as_view(form_class=CustomPasswordResetForm),name="password_reset"),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(form_class=CustomPasswordSetForm),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
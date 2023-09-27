from django.contrib import admin
from django.urls import path, include
from gaminghubwebsiteapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('forgot-password', views.forgotpass, name="forgotpass"),
    path('reset-password', views.resetpass, name="resetpass"),
    path('my-profile', views.profile, name="profile"),
    path('play-chess', views.chess, name="chess"),
    path('userregister', views.loguser, name="loguser"),
    path('loginuser', views.loginuser, name="loginuser"),
    path('verify-email', views.verifyemail, name="verifyemail"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('verify-link', views.verifylink, name="verifylink"),
    path('otp-valid', views.verifyotp, name="verifyotp"),
    path('code-generate', views.generate_code, name="generate_code"),
    path('schedule-game', views.game_schedule, name="game_schedule"),
    path('contact-us', views.contact_back, name="contact_back"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

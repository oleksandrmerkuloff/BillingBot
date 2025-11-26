from django.urls import path

from accounts.views import TelegramUserRegisterView


urlpatterns = [
    path("register/", TelegramUserRegisterView.as_view()),
]

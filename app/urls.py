from django.urls import path
from .views import SendEmailView, SendEmailToVeeva

urlpatterns = [
    path('', SendEmailToVeeva.as_view())
]

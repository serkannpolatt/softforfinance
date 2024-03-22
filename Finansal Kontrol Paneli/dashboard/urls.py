from django.urls import path
from .views import display_ticker

app_name = "dashboard"

urlpatterns = [
    path("<str:ticker>/", display_ticker, name="display_ticker"),
]
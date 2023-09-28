from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("profile/<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]

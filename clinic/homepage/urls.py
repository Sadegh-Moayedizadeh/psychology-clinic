from django.urls import path
from homepage import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("edit/<str:title>/", views.edit_content, name="edit_content"),
]

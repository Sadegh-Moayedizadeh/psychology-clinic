from django.urls import path

from clinic.apps.homepage import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("edit/<str:title>/", views.edit_content, name="edit_content"),
    path("edit/", views.get_edit_list, name="edit_list"),
]

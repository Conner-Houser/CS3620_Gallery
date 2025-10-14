from django.urls import path

from . import views

urlpatterns = [
    path("", views.ImageListView.as_view(), name="image_list"),
    path('upload/', views.UploadImageView.as_view(), name="image_upload"),
    path("my-gallery/", views.PersonalGalleryView.as_view(), name="personal_gallery"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.ImageListView.as_view(), name="image_list"),
    path('upload/', views.UploadImageView.as_view(), name="image_upload"),
    path("my-gallery/", views.PersonalGalleryView.as_view(), name="personal_gallery"),
    path("image/<int:pk>/", views.ImageDetailView.as_view(), name="image_detail"),
    path("history/", views.ViewHistoryView.as_view(), name="view_history"),

]   

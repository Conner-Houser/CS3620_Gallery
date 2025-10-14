from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ImageForm
from .models import Image

# Create your views here.
class UploadImageView(CreateView):
    template_name = "gallery/upload_image.html"
    model = Image
    fields = ["image"]
    success_url = "/my-gallery/"

    def form_valid(self, form):
        if not self.request.session.session_key:
            self.request.session.create()

        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)

class ImageListView(ListView):
    model = Image
    template_name = "gallery/Image_list.html"
    context_object_name = "images"

    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session.create()
        return super().get_queryset()

class PersonalGalleryView(ListView):
    model = Image
    template_name = "gallery/personal_gallery.html"
    context_object_name = "images"

    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session.create()
        # Only show images uploaded in this session
        return Image.objects.filter(session_key=self.request.session.session_key)
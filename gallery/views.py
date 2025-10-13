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
    fields = "__all__"
    success_url = "/"

class ImageListView(ListView):
    model = Image
    template_name = "gallery/Image_list.html"
    context_object_name = "images"


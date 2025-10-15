from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect

from .forms import ImageForm
from .forms import CommentForm
from .models import Image

# Create your views here.
class UploadImageView(CreateView):
    template_name = "gallery/upload_image.html"
    model = Image
    fields = ["image", "tags"]
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
    
        queryset = super().get_queryset()
        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
        return queryset

class PersonalGalleryView(ListView):
    model = Image
    template_name = "gallery/personal_gallery.html"
    context_object_name = "images"

    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session.create()

        queryset = Image.objects.filter(session_key=self.request.session.session_key)
    
        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
        return queryset


class ImageDetailView(DetailView):
    model = Image
    template_name = "gallery/image_detail.html"
    context_object_name = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = self.object
            comment.save()
            return redirect("image_detail", pk=self.object.pk)
        else: 
            print(form.errors)
        
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if not request.session.session_key:
            request.session.create()

        image_id = str(self.object.id)

        viewed = request.session.get("viewed_images", [])

        if image_id not in viewed:
            viewed.append(image_id)

        request.session["viewed_images"] = viewed

        return response
    

class ViewHistoryView(ListView):
    model = Image
    template_name = "gallery/view_history.html"
    context_object_name = "images"

    def get_queryset(self):
        viewed_ids = self.request.session.get("viewed_images", [])
        return Image.objects.filter(id__in=viewed_ids)
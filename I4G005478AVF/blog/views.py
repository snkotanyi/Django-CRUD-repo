from django.urls import reverse_lazy
from pkgutil import ImpImporter
from venv import create
from django.views.generic.list import ListView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")

from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from .forms import PostForm
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_thing"] = "Hello world :P this is dynamic"
        context["posts"] = Post.objects.all().order_by("-id")
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        new_object = Post.objects.create(text=form.cleaned_data["text"], image = form.cleaned_data["image"], description = form.cleaned_data["description"])
        messages.add_message(self.request, messages.SUCCESS, "Your post was successfully loaded")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.add_message(self.request, messages.FAILURE, "Your post was not successfully loaded")
        return super().form_invalid(form)

class DeletePostView(DeleteView):
    model = Post 
    template_name="confirm_delete.html"
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, "Your post was successfully deleted")
        return super().delete(request, *args, **kwargs)

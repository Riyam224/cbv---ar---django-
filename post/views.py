from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


# def post_list(request):
#     post_list = Post.objects.all()
#     return render(request, 'post_list.html', {'post_list': post_list})

# def post_details(request, post_id):
#     pass


# ************************** cbv

class PostList(ListView):

    model = Post
    template_name = 'post_list.html'
    # ! by default its name object_list
    # context_object_name = 'post_list'
    # context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)

    # like queryset
    def get_queryset(self):
        return Post.objects.filter(active=True)
    # like context object name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = 'sophie'
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'
    success_url = '/'


class PostCreate():
    pass


class PostDelete():
    pass


class PostUpdate():
    pass

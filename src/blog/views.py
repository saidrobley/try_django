from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_detail_view(request, slug):
    #obj = BlogPost.objects.get(id=post_id)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects
    # use a form
    template_name = 'blog/create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/updat.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)

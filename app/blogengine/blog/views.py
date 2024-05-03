from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Post , Tag
from django.views.generic import View
from .utils import ObjectDetailMixin,ObjectUpdateMixin
from .forms import TagForm
from .forms import PostForm


def posts_list(request):
    posts = Post.objects.all
    n = ['Oleg' , 'Masha' , 'Kit' ]
    return render(request, 'blog/index.html',context ={'posts' : posts})



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context = {'tags':tags})

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

    # def get(self,request,slug):
    #         post = get_object_or_404(Post,slug__iexact=slug)
    #         return render(request, 'blog/post_detail.html', context = {'post': post})

class PostCreate(View):
    def get(self,request):
        form = PostForm()
        return render(request, "blog/post_create.html", context = {'form':form})

    def post(self,request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, "blog/post_create.html", context = {'form':bound_form})


class PostUpdate(ObjectUpdateMixin,View):
        model  = Post
        model_form = PostForm
        template = 'blog/post_update_form.html'


class Tag_detail(ObjectDetailMixin,View):

    model = Tag
    template =  'blog/tag_detail.html'
    #  def get(self,request,slug):
    #         tag = get_object_or_404(Tag, slug__iexact=slug)
    #         return render (request, 'blog/tag_detail.html', context = {'tag':tag} )




class TagCreate(View):
    def get(self,request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context= {'form':form})

    def post(self,request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form':bound_form})


class TagUpdate(ObjectUpdateMixin,View):
    model  = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    # def get(self,request,slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render (request,'blog/tag_update_form.html', context = {'form':bound_form, 'tag':tag})

    # def post(self,request,slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm( request.POST , instance=tag)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form' , context = {'form':bound_form , 'tag': tag})

# Create your views here.

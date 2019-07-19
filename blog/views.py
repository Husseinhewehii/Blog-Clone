from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from . import models,forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import(
    TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
)

class About_View(TemplateView):
    template_name = 'about.html'


class Post_List_View(ListView):
    model = models.Post
    #ordering = ['-publish_date']

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class Post_Detail_View(DetailView):
    model = models.Post

class Post_Create_View(LoginRequiredMixin,CreateView):
    model = models.Post
    
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.Post_Form


class Post_Update_View(LoginRequiredMixin,UpdateView):
    model = models.Post

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.Post_Form

class Post_Delete_View(LoginRequiredMixin,DeleteView):
    model = models.Post

    success_url = reverse_lazy('blog:post_list')

class Draft_List_View(LoginRequiredMixin,ListView):
    model = models.Post

    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__isnull=True).order_by('-create_date')



########################## 
##########################

@login_required
def add_comment_to_post(req,pk):
    post = get_object_or_404(models.Post,pk=pk)
    if req.method == 'POST':
        form  = forms.Comment_Form(req.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = forms.Comment_Form()
    return render(req,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(req,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(req,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

@login_required
def post_publish(req,pk):
    post = get_object_or_404(models.Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)
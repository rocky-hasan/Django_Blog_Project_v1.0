from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from .models import Post,Category,Comment
from .forms import PostForm,CommentForm
from django.views.generic import ListView, DeleteView,DetailView,UpdateView,CreateView,TemplateView,View

# Create your views here.
def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model=Post
    context_object_name='posts'
    template_name='home.html'
    ordering=['-post_date']
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

def categorylistview(request):
    cat_menu_list=Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})


def categoryview(request, cats):
    category_posts=Post.objects.filter(category=cats)
    cat_menu=Category.objects.all()
    return render(request, 'categories.html',{'cats':cats.title(), 'category_post':category_posts,'cat_menu':cat_menu})


class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()    
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked-True

        context['total_likes']=total_likes
        context['cat_menu']=cat_menu
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'    -------when form_class using dont need (fields)
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url =reverse_lazy('home')

class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html'
    fields='__all__' 

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

class UpdatePostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='update_post.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(UpdatePostView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(DeletePostView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context
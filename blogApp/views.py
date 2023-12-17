from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





# List View
class PostListView(ListView):
    model = Post
    template_name =  'blogApp/home.html' # <app>/<model>_<viewtype>.html is default convention. But we are chaning it
    context_object_name = 'posts'
    ordering = ['-date_posted']  # orders post by date field, - means descending
    paginate_by = 5 # 2 posts per page
    
# Detail View
class PostDetailView(DetailView):
    model=Post


# LoginRequiredMixin is used to access create post view only if user is logged in. We cannot use decorators in class so we use this mixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    # Overriding form_valid function to set Post uthor_id to current loggred in users author_id
    # CHECK MODELS.PY ABOUT GET_ABSOLUTE URL
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs form_valid method on parent class
    
# We need not create a template for update. Django uses the create post_form for both create and udpate template 
# We use UserPassesTestMixin so that not any user can update any other users post
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs form_valid method on parent class  
    
    #  Over riding test_func in UserPass mixin. 
    def test_func(self):
        post = self.get_object()
        
        #Only if current user is the author we allow to update
        if self.request.user == post.author:
            return True
        return False

# Delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url = "/" # After deletion goes to home page
    
    # Only logged in user can delete their post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
def about(request):
    context = {
        'title' : 'About page context'
    }
    return render(request, 'blogApp/about.html', context)
    











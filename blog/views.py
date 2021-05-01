from django.shortcuts import render, get_object_or_404
from .forms import CommentForm, SignUpForm
from django.views import generic
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.urls import  reverse_lazy


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted


    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class BlogUpdateView(generic.UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'content']

class BlogCreateView(generic.CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'slug', 'author', 'content', 'status']

class BlogDeleteView(generic.DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
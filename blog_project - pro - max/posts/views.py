from django.shortcuts import render, redirect, get_object_or_404
from .import forms, models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView


# Create your views here.
# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST)
#         post_form.instance.author = request.user
#         if post_form.is_valid():
#             post_form.save()
#             return redirect("Home")
#     else:
#         post_form = forms.PostForm()
#     return render(request, 'add_post.html', {'form':post_form})

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('Home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk = id)
#     post_form = forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST)
#         post_form.instance.author = request.user
#         if post_form.is_valid():
#             post_form.save()
#             return redirect("Home")
#     return render(request, 'add_post.html', {'form':post_form})
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('Home')
    pk_url_kwarg = 'id'

# @login_required
# def delete_post(request, id):
#     post = models.Post.objects.get(pk = id)
#     post.delete()
#     return redirect("Home")
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('Home')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = forms.CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, pk=kwargs['id'])
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_details', id=post.id)
        comments = post.comments.all()
        return render(request, self.template_name, {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        })
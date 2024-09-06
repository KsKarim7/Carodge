from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DeleteView

# Create your views here.
# @method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)
    
# @method_decorator(login_required, name='dispatch')
# class DeleteCarView(DeleteView):
#     model = models.Car
#     template_name = 'delete.html'
#     success_url = reverse_lazy('profile')
#     pk_url_kwarg = 'id'


# class DetailPostView(DetailView):
#     model = models.Post
#     template_name = 'post_details.html'
    
#     def post(self, request, *args, **kwargs):
#         comment_form = forms.CommentForm(data=self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#         return self.get(request, *args, **kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object #storing post model object
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()
        
#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context
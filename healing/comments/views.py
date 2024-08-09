from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from comments.models import Comments
from comments.forms import CommentsForm


class CommentsListView(LoginRequiredMixin, ListView):
    model = Comments
    template_name = 'pages/comments.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentsForm()
        context['comments'] = Comments.objects.all().order_by('-created_at')
        return context


class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'pages/comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("comments:list_comment")


class CommentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'pages/delete_comments.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.object
        return context

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comments, pk=self.kwargs["comment_id"])
        if comment.author != self.request.user:
            raise PermissionDenied
        return comment

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comments:list_comment')


class CommentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    template_name = 'pages/delete_comments.html'
    context_object_name = 'comment'

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comments, pk=self.kwargs["comment_id"])
        if comment.author != self.request.user:
            raise PermissionDenied
        return comment

    def get_success_url(self):
        return reverse_lazy('comments:list_comment')

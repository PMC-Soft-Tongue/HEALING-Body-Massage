from django.urls import path
from comments.views import CommentsUpdateView, CommentsDeleteView, CommentsListView, CommentsCreateView

app_name = 'comments'

urlpatterns = [
    path('edit_comment/<int:comment_id>/', CommentsUpdateView.as_view(), name='edit_comment'),
    path('delete_comment/<int:comment_id>/', CommentsDeleteView.as_view(), name='delete_comment'),
    path('add_comment/', CommentsCreateView.as_view(), name='add_comment'),
    path('', CommentsListView.as_view(), name='list_comment'),
]

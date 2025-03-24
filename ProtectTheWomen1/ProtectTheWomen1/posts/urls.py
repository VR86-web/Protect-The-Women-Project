from django.urls import path, include

from ProtectTheWomen1.posts import views
from ProtectTheWomen1.posts.views import AddPostView, AllPostView, UpdatePostView, DeletePostView, DetailPostView

urlpatterns = [
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('all-posts/', AllPostView.as_view(), name='all-posts'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post-detail'),
    path('<int:pk>/', include([
        path('comment/', views.CommentCreateView.as_view(), name='comment'),
        path('comment/<int:comment_id>/reply/', views.reply_to_comment, name='reply'),
        path('like/', views.likes_functionality, name='like'),
        path('update-post/', UpdatePostView.as_view(), name='update-post'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
    ])),
]



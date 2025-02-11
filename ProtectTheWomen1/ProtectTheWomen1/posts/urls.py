from django.urls import path, include

from ProtectTheWomen1.posts import views
from ProtectTheWomen1.posts.views import AddPostView, AllPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('all-posts/', AllPostView.as_view(), name='all-posts'),
    path('<int:pk>/', include([
        path('comment/', views.CommentCreateView.as_view(), name='comment'),
        path('update-post/', UpdatePostView.as_view(), name='update-post'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
    ])),

]

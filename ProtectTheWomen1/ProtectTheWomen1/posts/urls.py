from django.urls import path, include

from ProtectTheWomen1.posts.views import AddPostView, AllPostView, UpdatePostView

urlpatterns = [
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('all-posts/', AllPostView.as_view(), name='all-posts'),
    path('<int:pk>/', include([
        path('update-post/', UpdatePostView.as_view(), name='update-post'),
    ])),

]

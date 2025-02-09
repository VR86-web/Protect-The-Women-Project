from django.urls import path, include

from ProtectTheWomen.posts import views

urlpatterns = [
    path('add_post/', views.AddPost.as_view(), name='add-post'),
    path('posts-list/', views.posts_list, name='posts-list'),
    path('<int:pk>/', include([
        path('delete-post/', views.DeleteView.as_view(), name='delete-post'),
        path('update_post/', views.UpdatePost.as_view(), name='update-post'),
        path('single_post/', views.DetailsPost.as_view(), name='single-post'),
    ]))
]
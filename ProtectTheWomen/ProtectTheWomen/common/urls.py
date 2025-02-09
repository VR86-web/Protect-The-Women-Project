from django.urls import path

from ProtectTheWomen.common import views

urlpatterns = [
    path('', views.index, name='home'),
    path('comment/<int:post_id>/', views.comment_functionality, name='comment'),
    path('like/<int:post_id>/', views.comment_functionality, name='like'),
]
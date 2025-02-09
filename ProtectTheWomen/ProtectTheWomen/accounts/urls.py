from django.contrib.auth.views import LogoutView
from django.urls import path, include

from ProtectTheWomen.accounts import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details_page, name='profile-details'),
        path('edit/', views.ProfileEdit.as_view(), name='profile-edit'),
        path('delete/', views.profile_delete_page, name='profile-delete'),
    ])),
]
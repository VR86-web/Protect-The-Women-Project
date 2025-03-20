
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from ProtectTheWomen1.accounts.views.user_views import UserRegisterView, UserLoginView
from ProtectTheWomen1.accounts.views.profile_views import ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView, ProfileCreateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile_create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/', include([
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]


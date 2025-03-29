from django.urls import path

from ProtectTheWomen1.common.views import HomePage, AboutView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]

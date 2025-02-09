from django.urls import path

from ProtectTheWomen1.common import views

urlpatterns = [
    path('', views.home_page, name='index'),

]
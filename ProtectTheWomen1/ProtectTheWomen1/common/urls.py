from django.urls import path

from ProtectTheWomen1.common import views
from ProtectTheWomen1.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),

]
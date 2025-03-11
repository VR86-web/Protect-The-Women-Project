
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ProtectTheWomen1.accounts.forms import ProfileCreateForm
from ProtectTheWomen1.posts.models import Post


# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(ListView, BaseFormView):
    model = Post
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common_templates/index.html']
        return ['common_templates/index-without-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

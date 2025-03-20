from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ProtectTheWomen1.accounts.forms import ProfileCreateForm
from ProtectTheWomen1.common.models import News
from ProtectTheWomen1.posts.models import Post


class HomePage(ListView, BaseFormView):
    model = Post
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common_templates/index.html']
        return ['common_templates/index-without-profile.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_items'] = News.objects.all().order_by('-created_at')
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

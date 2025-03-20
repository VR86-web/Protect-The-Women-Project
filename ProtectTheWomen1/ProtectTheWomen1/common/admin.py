from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image')
    search_fields = ('title', 'content')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='news_writers').exists():
            return queryset
        return queryset.none()

    def has_add_permission(self, request):
        return request.user.groups.filter(name='news_writers').exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='news_writers').exists() or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='news_writers').exists() or request.user.is_superuser


admin.site.register(News, NewsAdmin)


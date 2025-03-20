from django.contrib import admin

from ProtectTheWomen1.posts.models import Post, Comment, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'content', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'user', 'created_at')
    search_fields = ('author', 'content', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_post')
    list_filter = ('to_post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)

from django.contrib import admin
from .models import Post, Group, Comment, Favorite
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", "group") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-"

admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "description", "title", "slug") 
    search_fields = ("description", "title") 
    empty_value_display = "-пусто-"

admin.site.register(Group, GroupAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "text", "created", "author")
    search_fields = ("text",) 
    list_filter = ("post", "author", "created") 
    empty_value_display = "-пусто-"

admin.site.register(Comment, CommentAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "author")
    list_filter = ("user", "author")

admin.site.register(Favorite, FavoriteAdmin)
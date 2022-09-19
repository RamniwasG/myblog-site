from django.contrib import admin
from .models import Post, Auther, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ("auther", "date", "tags",)
    list_display = ("title", "date", "auther")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Auther)
admin.site.register(Tag)

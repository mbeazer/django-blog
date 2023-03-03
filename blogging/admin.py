from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdminInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryAdminInline]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryAdminInline]
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

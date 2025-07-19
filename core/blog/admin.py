from django.contrib import admin
from .models import Category, Post

# Register Post model.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'category', 'status')
    list_filter = ('status', 'category')
    ordering = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model= Category
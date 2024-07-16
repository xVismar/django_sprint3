from django.contrib import admin
from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class CategoryInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        CategoryInline,
    )
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'created_at',
        'pub_date',
        'category',
        'location',
        'is_published',
        'title',
        'text'
    )

    list_editable = (
        'is_published',
        'category',
        'location',
    )

    list_filter = (
        'category',
        'author',
        'location',
    )

    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)

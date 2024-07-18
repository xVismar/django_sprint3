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
        'is_published'
    )
    list_editable = (
        'is_published',
    )


class LocationInline(admin.StackedInline):
    model = Post
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        LocationInline,
    )
    list_display = (
        'name',
        'is_published'
    )
    list_editable = (
        'is_published',
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
        'short_text'
    )

    list_editable = (
        'is_published',
        'category',
        'location',
        'pub_date',
    )

    list_filter = (
        'category',
        'author',
        'location',
    )

    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)

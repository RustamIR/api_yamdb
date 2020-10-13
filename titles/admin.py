from django.contrib import admin
from titles.models import Categories, Genres, Titles


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    search_fields = ("name",)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    search_fields = ("name",)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "description", 'category')
    search_fields = ("name",)
    empty_value_display = '-пусто-'


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Genres, GenreAdmin)
admin.site.register(Titles, TitleAdmin)


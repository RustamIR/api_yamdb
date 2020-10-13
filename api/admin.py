from django.contrib import admin

from api.models import Comment, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author", "score",
                    'pub_date', 'title', 'title_id')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author", 'pub_date', 'review', 'review_id')
    empty_value_display = '-пусто-'



admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

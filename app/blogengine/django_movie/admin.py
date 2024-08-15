from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Labl", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 0
    ## readonly_fields = ("email", "name",)


class MovieShortsInlite(admin.TabularInline):
    model = MovieShots
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"  >')

    get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


# @admin.action(description="Опубликовать")
# def unpublish(self, request, queryset):
#     row_update = queryset.update(draft=True)
#     if row_update == 1:
#         message_bit = "1 запись была обновлена"
#     else:
#         message_bit = f"обновлено записей  {row_update} "
#     self.message_user(request, f"{message_bit}")


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ("id", "title", "category", "url", "draft",)
    list_display_links = ("title",)
    list_filter = ("category", "year",)
    search_fields = ("title", "category__name",)
    inlines = [MovieShortsInlite, ReviewInLine]
    save_on_top = True
    save_as = True
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    ## отображение полей в режиме редактирования
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": (("description"),)
        }),
        (None, {
            "fields": (("poster"),)
        }),
        (None, {
            "fields": (("get_image"),)
        }),
        (None, {
            "fields": (("year", "country", "world_premiere"),)
        }),
        (None, {
            "fields": (("actors", "directors"),)
        }),
        (None, {
            "fields": (("genres", "category"),)
        }),
        ("Budget", {
            "classes": ("collapse",),
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Urls", {
            "fields": (("video_url", "url"),)
        }),
        (None, {
            "fields": (("draft"),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="150"  >')

    get_image.short_description = "Постер"

    @admin.action(description=" Не опубликовать")
    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"обновлено записей  {row_update} "
        self.message_user(request, f"{message_bit}")

    @admin.action(description="Опубликовать")
    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = " 1 запись была обновлена"
        else:
            message_bit = f"обновлено записей  {row_update} "
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Убрать публикацию"
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "movie", "parent", "text",)
    list_display_links = ("email",)
    readonly_fields = ("email", "name",)


@admin.register(MovieShots)
class MovieShortsAdmin(TranslationAdmin):
    list_display = ("title", "description", "get_image", "movie",)
    list_display_links = ("title",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"  >')

    get_image.short_description = "Изображение"


@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    list_display = ("name", "age", "description", "get_image",)
    list_display_links = ("name",)
    search_fields = ("name",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"  >')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display = ("name", "description", "url",)
    list_display_links = ("name",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip", "movie", "star",)
    list_display_links = ("ip",)


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("value",)
    list_display_links = ("value",)


admin.site.site_title = "Movies"
admin.site.site_header = "Movies"

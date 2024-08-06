from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre,Movie, MovieShots,Actor,Rating,RatingStar,Reviews


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
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","url")
    list_display_links = ("name",)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id","title","category","url","draft", )
    list_display_links = ("title",)
    list_filter = ("category","year",)
    search_fields = ("title","category__name",)
    inlines = [MovieShortsInlite,ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
     ## отображение полей в режиме редактирования
    fieldsets = (
        (None,{
        "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": (("poster"),)
        }),
        (None, {
            "fields": (("get_image"),)
        }),
        (None, {
            "fields": (("year", "country","world_premiere"),)
        }),
        (None,{
            "fields": (("actors" , "directors"),)
        }),
        (None, {
        "fields": (("genres", "category"),)
        }),
        ("Budget" ,{
            "classes": ("collapse",),
            "fields": (("budget","fees_in_usa","fees_in_world"),)
        }),
        ("Urls",{
            "fields": (("video_url","url"),)
        }),
        (None,{
            "fields": (("draft"),)
        })
    )
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="150"  >')

    get_image.short_description = "Постер"




@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "movie","parent", "text",)
    list_display_links = ("email",)
    readonly_fields = ("email" , "name" ,)


@admin.register(MovieShots)
class MovieShortsAdmin(admin.ModelAdmin):
    list_display = ("title", "description" ,"get_image" ,"movie",)
    list_display_links = ("title",)
    readonly_fields = ("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"  >')

    get_image.short_description = "Изображение"




@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name","age","description","get_image",)
    list_display_links = ("name",)
    search_fields = ("description",)
    readonly_fields = ("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"  >')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url",)
    list_display_links = ("name",)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip","star","movie",)
    list_display_links = ("ip",)

@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("value",)
    list_display_links = ("value",)


admin.site.site_title = "Movies"
admin.site.site_header = "Movies"




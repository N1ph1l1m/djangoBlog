from django.contrib import admin

from .models import Category, Genre,Movie, MovieShots,Actor,Rating,RatingStar,Reviews


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 0
    ## readonly_fields = ("email", "name",)

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
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
     ## отображение полей в режиме редактирования
    fieldsets = (
        (None,{
        "fields": (("title", "tagline"),)
        }),
        (None,{
            "fields": (("description"),)
        }),
        (None, {
            "fields": (("poster"),)
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




@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "movie","parent", "text",)
    list_display_links = ("email",)
    readonly_fields = ("email" , "name" ,)


@admin.register(MovieShots)
class MovieShortsAdmin(admin.ModelAdmin):
    list_display = ("title", "description" ,"image" ,"movie",)
    list_display_links = ("title",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name","age","description","image",)
    list_display_links = ("name",)
    search_fields = ("description",)

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





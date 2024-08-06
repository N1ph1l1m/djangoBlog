from django.apps import AppConfig


class DjangoMovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_movie'
    verbose_name = "Фильмы"

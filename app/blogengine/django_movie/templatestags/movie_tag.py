from django import template

from app.blogengine.django_movie.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()

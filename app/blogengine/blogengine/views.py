from django.http import HttpResponse
from django.shortcuts import redirect


# def redirect_blog(request):
#     return redirect('posts_list_url', permanent=True)
# def redirect_blog(request):
#     return redirect('movie_list', permanent=True)


def test(request):
    return HttpResponse("Test django_movie")
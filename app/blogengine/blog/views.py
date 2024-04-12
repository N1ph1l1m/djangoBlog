from django.shortcuts import render


def posts_list(request):
    n = ['Oleg' , 'Masha' , 'Kit' ]
    return render(request, 'blog/index.html',context={'name' : n})


# Create your views here.

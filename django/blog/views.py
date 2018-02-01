from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # 1. browser requests
    # 2. runserver receives request
    # 3. runserver delivers request to Django code
    # 4. config.urls in Django code receives request
    # 5. config.urls module delivers every requests except ''(admin/) to blog.urls module
    # 6. blog.urls looks for whether there's the same pattern with received requests
    # 7. if it is, execute connected function(view)
    #   7-1. from TEMPLATES attribute inside settings module, search DIRS list for finding blog/post_list.html
    #   7-2. render() found html(blog/post_list.html) and return it
    # 8. deliver the return value of function(view) to the browser

    # return text-data response as HTTP protocol
    # return HttpResponse('<html><body><h1>post list</h1><p>Post list will be here</p></body></html>')

    # return 'blog/post_list.html' template file as HTTP protocol
    return render(request, 'blog/post_list.html')

def post_detail(request):

    return render(request, 'blog/post_detail.html')
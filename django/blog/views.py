from django.http import HttpResponse


def post_list(request):
    # 1. browser requests
    # 2. runserver receives request
    # 3. runserver delivers request to Django code
    # 4. config.urls in Django code receives request
    # 5. config.urls module delivers every requests except ''(admin/) to blog.urls module
    # 6. blog.urls looks for whether there's the same pattern with received requests
    # 7. if it is, execute connected function(view)
    # 8. deliver the return value of function(view) to the browser


    # return text-data response as HTTP protocol
    return HttpResponse('<html><body><h1>post list</h1><p>Post list will be here</p></body></html>')

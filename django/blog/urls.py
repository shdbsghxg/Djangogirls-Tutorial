import re
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    # path('', views.post_detail),
    re_path(r'(?P<pk>\d+)/$', views.post_detail),
    # regex for at least 1 num
    # group the repeated part named 'pk'
    # -> re.compile(r'(?P<pk>\d+)')
]

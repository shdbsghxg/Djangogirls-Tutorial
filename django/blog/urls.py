import re
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    # path('', views.post_detail),

    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('<int:pk>/', views.post_detail, name='post-detail'),


    # path for localhost:8000/add
    path('add', views.post_add, name='post-add'),



    # regex for at least 1 num
    # group the repeated part named 'pk'
    # -> re.compile(r'(?P<pk>\d+)')
]

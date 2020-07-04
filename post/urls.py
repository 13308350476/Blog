# coding = utf-8
from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.queryAll),
    re_path('page/(\d+)', views.queryAll),
    re_path('post/(\d+)', views.detail),
    re_path('category/(\d+)', views.queryPostByCid),
    re_path('archive/(\d+)/(\d+)', views.queryPostByCreated),
]

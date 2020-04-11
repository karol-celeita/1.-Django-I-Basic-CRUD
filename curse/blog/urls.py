from django.urls import path
from .  views import*

urlpatterns = [


	path('',blog_post_list_view,name='blog_all'),
	path('blog-new/',blog_post_create_view, name='blog_nuevo'),
	path('blog/<str:slug>/',blog_post_detail_view, name='blog_detalle'),
	path('blog/<str:slug>/edit/',blog_post_update_view, name='blog_update'),
	path('blog/<str:slug>/delete/',blog_post_delete_view, name='blog_delete'),
]


"""URLS AND LOOKUPS"""
 # 1. ID con expresiones regulares: re_path(r'^blog/(?P<post_id>\d+)/$',blog_post_detail_page)
 # 2. ID sin regex: path('blog/<int:post_id>/',blog_post_detail_page),
 # 3. ID con regex y slug para cambiar la url: re_path(r'^blog/(?P<slug>\w+)/$',blog_post_detail_page)
 # 4. ID sin regex y con slug: path('blog/<str:slug>/',blog_post_detail_page),
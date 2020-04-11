from django.shortcuts import render

from .models import *
from blog.models import PostBlog

def search_view(request):

	query=request.GET.get('q',None)
	context={'query':query}
	user=None
	if request.user.is_authenticated:
		user=request.user

	if query is not None:

		SearchQuery.objects.create(user=user,query=query)
		blog_list=PostBlog.objects.search(query=query)
		context['blog_list']=blog_list

	return render(request,'search_view.html',context)
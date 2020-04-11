from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

from .models import *
from .forms import *



#EXAMPLE ONE
# def blog_post_detail_page(request,slug):
# 	obj=get_object_or_404(PostBlog.objects.filter(slug=post_id))
# 	template_name='blog_post_detail.html'
# 	context={"object":obj}
# 	return render(request,template_name,context)

"""DETALLES IMPORTANTES
	1. (request,post_id): parametro por url 
	2.  print(post_id.__class__) #Muestra el tipo de dato de un parametro url

	3.	try:
			obj=PostBlog.objects.get(id=post_id)
		except PostBlog.DoesNotExist:
			raise Http404
		except ValueError:
			raise Http404

	4. Se puede reemplazar el try mediante el metodo get_object_or_404

	5. Para usar el slug usamos el objects.filter y la instancia para corregir el error de varios registros

	"""
# ----------------------------------------------------
"""CRUD"""

def blog_post_list_view(request):

	qs=PostBlog.objects.all().published()  #queryset manager del modelo
	if request.user.is_authenticated:
		ps=PostBlog.objects.filter(user=request.user)
		qs=(qs|ps).distinct()

	context={"object_list":qs}
	template_name='blog_post_list.html'
	return render(request,template_name,context)

# ----------------------------------------------------

# @staff_member_required
@login_required(login_url='/login')
def blog_post_create_view(request):

	# if not request.user.is_authenticated:
	# 	return render(request,template_name,context)

	form=BlogPostForm(request.POST or None,request.FILES or None)

	if form.is_valid():
		obj=form.save(commit=False)
		obj.user=request.user
		obj.save()

		form=BlogPostForm()
		return redirect('../')

	context={"form":form}
	template_name='blog_post_create.html'
	return render(request,template_name,context)


# ----------------------------------------------------

def blog_post_detail_view(request,slug):

	obj=get_object_or_404(PostBlog,slug=slug)
	template_name='blog_post_detail.html'
	context={"object":obj}
	return render(request,template_name,context)

# ----------------------------------------------------

def blog_post_update_view(request,slug):

	obj=get_object_or_404(PostBlog,slug=slug)
	form=BlogPostForm(request.POST or None, instance=obj)

	if form.is_valid():
		form.save()

	template_name='blog_post_update.html'
	context={"form":form,"title":f"Actualizar{ obj.title}"} #f se utiliza para poner strings

	return render(request,template_name,context)

# ----------------------------------------------------

def blog_post_delete_view(request,slug):

	obj=get_object_or_404(PostBlog,slug=slug)
	template_name='blog_post_delete.html'

	if request.method=='POST':
		obj.delete()
		# return redirect("../")

	context={"object":obj}
	return render(request,template_name,context)
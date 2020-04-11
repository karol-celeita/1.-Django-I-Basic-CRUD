from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

User=settings.AUTH_USER_MODEL

#MODEL MANAGER AND CUSTOM QUERYSET: Gestores y conjuntos de consultas personalizadas
"""https://docs.djangoproject.com/en/3.0/topics/db/managers/#modifying-a-manager-s-initial-queryset
Por defecto, Django agrega un Managercon el nombre objectsa cada clase de modelo de Django.
 Sin embargo, si desea usarlo objects como un nombre de campo,
  o si desea usar un nombre que no sea objects para el Manager, 
  puede cambiarle el nombre según el modelo. 
  Para cambiar el nombre Manager de una clase determinada, 
  defina un atributo de clase de tipo models.Manager()en ese modelo.  """


"""La funcion search es la encargada de buscar en la barra de busqueda del menu"""		
class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now=timezone.now()
		return self.filter(publish_date__lte=now)
	def search(self,query):
		lookup = (Q(title__icontains=query)|
				  Q(content__icontains=query)|
				  Q(slug__icontains=query)|
				  Q(user__username__icontains=query)
				  )	

		return self.filter(lookup)

class BlogPostManager(models.Manager):

	def get_queryset(self):
		return BlogPostQuerySet(self.model,using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)
# ------------------------------------------------------------------

class PostBlog(models.Model):

	# slug hace que la url sea visualmente mejor
	user=models.ForeignKey(User,default=1, on_delete=models.CASCADE)
	title=models.TextField()
	content=models.TextField(null=True, blank=True)
	slug=models.SlugField(unique=True)
	publish_date=models.DateTimeField(auto_now=False,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	image=models.FileField(upload_to='image/', blank=True,null=True)
	pillow=models.ImageField(upload_to='image/', blank=True,null=True)
	objects =BlogPostManager()

# ----------------------------------------------------------------
# Se usa para enviar la url completa en el template listview
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		 return reverse('blog_update', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return f"{self.get_absolute_url}/delete"


# Grabar datos desde el modelo 
# class Blog:
# 	title='Hello'
# 	content='How are you'

from django import forms
from.models import *


class BlogPostForm(forms.ModelForm):
	class Meta:
		model=PostBlog
		fields=['title','slug','pillow','content','publish_date']


# Para validar campos

	def clean_title(self,*args,**kwargs):

		instance=self.instance  #Se usa para que el formulario funcione para create y update sin poner el error de validacion

		title=self.cleaned_data.get("title")
		qs=PostBlog.objects.filter(title__iexact=title) #Para Validar mayusculas y minusculas

		if instance is not None:
			qs=qs.exclude(pk=instance.pk)


		if qs.exists():
			raise forms.ValidationError('Este nombre ya está en uso')
		return title





			
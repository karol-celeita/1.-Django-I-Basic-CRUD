from django.db import models
from django.conf import settings

# Create your models here.
class SearchQuery(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
	query=models.CharField(max_length=220)
	timestamp=models.DateTimeField(auto_now_add=True)
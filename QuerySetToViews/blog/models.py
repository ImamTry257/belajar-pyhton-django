from django.db import models

# Create your models here.
class Posts(models.Model):
	judul = models.CharField(max_length=255)
	body = models.TextField()
	category = models.CharField(max_length=255)
	post_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.judul)

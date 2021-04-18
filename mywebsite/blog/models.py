from django.db import models

# Create your models here.
class Post(models.Model):
	judul = models.CharField(max_length=200)
	# blank true -> boleh kosong pada form input
	body = models.TextField()
	email = models.EmailField(default='nama@email.com')
	alamat = models.CharField(max_length=255,blank=True)
	waktu_posting = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.judul)

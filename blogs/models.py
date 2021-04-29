from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
	name = models.CharField(max_length=250)
	active = models.BooleanField(default=False)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	cover = models.ForeignKey(
		'Cover',
		models.SET_NULL,
		blank=True,
		null=True
	)


class Cover(models.Model):
	name = models.TextField()
	description = models.CharField(max_length=25, blank=True, null=True)
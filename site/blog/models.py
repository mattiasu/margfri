from django.db import models

class Blogpost(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	intro = models.CharField(max_length=300)
	body = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.title
		

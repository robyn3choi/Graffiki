from django.db import models
from django.utils import timezone

# Graffiti class created by Wendy
class Graffiti(models.Model):
	photo = models.ImageField(upload_to='graffitiPics')
	description = models.TextField()
	lat = models.FloatField(default=49.2630182016568)
	lon = models.FloatField(default=-123.120131523468)
	count = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.lat) + "," + str(self.lon)
	
	def approved_comments(self):
		return self.comments.filter(approved=True)
		

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')

	
# Comment class created by Wendy
class Comment(models.Model):
	graffiti = models.ForeignKey('graffiki_app.Graffiti', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)

	
	def approve(self):
		self.approved = True
		self.save()
	
	def __str__(self):
		return self.text
	

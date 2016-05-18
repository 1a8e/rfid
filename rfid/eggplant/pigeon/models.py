from django.db import models

class Scroll(models.Model):
	scrollID = models.CharField('RFID', max_length=40)
	#scrollFrom = models.CharField('from', max_length=80)
	#scrollTo = models.CharField('to', max_length=80)
	scrollMessage = models.CharField('message', max_length=1024)
	#regDate = models.DateTimeField('date registered')
	#pubDate = models.DateTimeField('date published', blank=True, null=True)
	#published = models.BooleanField()

	def __str__(self):
		return self.scrollID

	# def s_from(self):
	# 	return scrollFrom

	# def s_to(self):
	# 	return scrollTo

	def s_message(self):
		return scrollMessage

	# def isPublished(self):
	# 	return self.published

	# def publish(self):
	# 	self.isPublished = True
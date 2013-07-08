from django.db import models

# Create your models here.
BOOLEAN_CHOICES = ((True, 'On'), (False, 'Off'))
class Light(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	#pub_date = models.DateTimeField()
	#likes = models.IntegerField()
	onOff = models.BooleanField(choices=BOOLEAN_CHOICES)
	
	
	def __unicode__(self):
		return self.title
		
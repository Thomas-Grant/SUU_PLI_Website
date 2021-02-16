from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Collection(models.Model):
	collection_id = models.TextField() #set regular expression
	plant_name = models.TextField()
	voucher_date = models.DateTimeField(default=timezone.now)
	location = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.collection_id
from django.db import models

class List(models.Model):
	name = models.CharField(max_length =200)
	description = models.CharField(max_length =400, null=True)
	additional = models.CharField(max_length =200, null=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' + self.description + ' | ' + self.additional + ' | ' + str(self.completed)

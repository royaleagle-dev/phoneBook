from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 255)
	phone = models.CharField(max_length = 255)
	date_added = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = 'contact'
		verbose_name_plural = 'contacts'
		ordering = ['last_name', 'address', 'first_name']

	def __str__(self):
		return self.first_name

	def hasPhone(self):
		if len(self.phone) > 1 and len(self.phone) <12:
			return True
		else:
			return False

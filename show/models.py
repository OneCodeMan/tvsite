from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Show(models.Model):
	owner = models.ForeignKey(User, null=True, default=True, related_name='o')
	title = models.CharField(max_length=100)
	description = models.TextField(default='N/A', blank=True, max_length=250)
	season = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
	episode = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

	def get_absolute_url(self):
		return reverse('show:index')

	def __str__(self):
		return self.title
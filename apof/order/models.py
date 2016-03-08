# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Restaurant (models.Model):
	"""
	Restaurant model.
	"""

	name = models.CharField('nazwa restauracji', max_length=255)
	address = models.CharField('adres restauracji', max_length=255)
	phone_number = models.CharField('numer telefonu', max_length=16)
	order_time_start =  models.TimeField('od godziny:')
	order_time_end =  models.TimeField('do godziny:')

	def __str__(self):
		return str(self.name)

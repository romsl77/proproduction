import uuid
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class WagonDrawing(models.Model):
	wagon_number = models.IntegerField(default=0)
	ok_date = models.DateField()
	link = models.CharField(max_length=300)
	product = models.CharField(max_length=30, blank=True)
	product_description = models.CharField(max_length=82, blank=True)
	wagon_id = models.CharField(max_length=32, blank=False)
	sortnr = models.IntegerField(default=0)
	position = models.CharField(max_length=15, blank=True)
	gfnr = models.CharField(max_length=10, blank=True)
	sequence = models.IntegerField(default=0)
	daycolor = models.CharField(max_length=8, blank=True)
	posart1_quantity = models.IntegerField(blank=True, default=0)
	iid = models.CharField(max_length=40, blank=False, default=0)
	
	def __str__(self):
		return self.link
	def show_ok_date(self):
		return self.ok_date
	def wagonnumber(self):
		return self.wagon_number

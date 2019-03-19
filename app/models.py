from django.db import models

class Foodstuff(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(max_length=100)
	foodstuffs = models.ManyToManyField(Foodstuff, blank=True,max_length=140, verbose_name='材料')
	text = models.TextField(blank=True)
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,blank=True, null=True)
   
	def __str__(self):
		return self.name
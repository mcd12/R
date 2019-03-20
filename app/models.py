from django.db import models


class Foodcategory(models.Model):
    name = models.CharField( max_length=255,verbose_name='料理の種類')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField( max_length=255,verbose_name='カテゴリ名')

    def __str__(self):
        return self.name

class Foodstuff(models.Model):
	name = models.CharField(max_length=100,verbose_name='主素材')
	category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,blank=True, null=True)

	def __str__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(max_length=100,verbose_name='料理名')
	foodstuffs = models.ManyToManyField(Foodstuff, blank=True,max_length=140, verbose_name='材料')
	# subfoodstuffs = models.ManyToManyField(Foodstuff, blank=True,max_length=140, verbose_name='その他材料')
	foodcategory = models.ForeignKey(Foodcategory,verbose_name='料理の種類',on_delete=models.PROTECT,blank=True, null=True)
	text = models.TextField(blank=True)
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,blank=True, null=True)
   
	def __str__(self):
		return self.name
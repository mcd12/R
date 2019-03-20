from django.contrib import admin
from .models import Food,Foodstuff,Category,Foodcategory

admin.site.register(Food)
admin.site.register(Foodstuff)
admin.site.register(Foodcategory)
admin.site.register(Category)
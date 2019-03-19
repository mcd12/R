
from django.views.generic import ListView
from .models import Food, Foodstuff,Category

class FoodListView(ListView):

    model =  Food
    q_foodstuffs = 'start'
    AAfoodstuffs = ''
    
    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        
        # 絞り込み条件の設定
        foodstuffs = Foodstuff.objects.all()
        context['foodstuffs'] = foodstuffs
        
        categorys = Category.objects.all()
        context['categorys'] = categorys

        C = []
        for category in categorys:
            B = category.foodstuff_set.all()
            D = {"name": category.name, "foodstuff": B}
            C.append(D)

        context['stuff'] = C
        context['q_foodstuffs'] = self.q_foodstuffs
        context['AAfoodstuffs'] = self.AAfoodstuffs
        return context
    
   

    def get_queryset(self):

        foods = self.model.foodstuffs
        
        q_foodstuffs = self.request.GET.getlist('foodstuff')
        self.q_foodstuffs = q_foodstuffs

        self.AAfoodstuffs = foods

        

    #     q_foodstuffs = self.request.GET.getlist('foodstuff')
    #     full = []
    #     minus_one = []
    #     print('lskdjflskdjflaaaaa' + q_foodstuffs)

    #     q_foodstuffs = map(lambda x: x.value, q_foodstuffs)

    #     for food in foods:
    #         count = food.foodstuffs.count()
    #         match_count = (food.foodstuffs & q_foodstuffs).count()

    #         if count - match_count == 0:
    #             full.append(food)
    #         elif count - match_count == 1:
    #             minus_one.append(food)



    #     #  q_foodstuffs = self.request.GET.getlist('foodstuff')
    #     #  o_foodstuffs = foods.foodstuff.count()
    #     #  c_foodstuffs = self.rewuest.GET.getlist('foodstuff').count('q_foodstuffs')


        if len(q_foodstuffs) != 0:
            foods = foods.filter(foodstuffs__in=q_foodstuffs).distinct()
            
    #     #  if len(q_foodstuffs) != 0:
    #     #     minus_one = foods.filter(foodstuffs__in=q_foodstuffs).distinct()


        # foods = {"full": full}

        return foods

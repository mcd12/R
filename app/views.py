
from django.views.generic import ListView
from django.db.models import Count
from .models import Food, Foodstuff,Category


class FoodListView(ListView):

    model =  Food
    context_object_name = "food"

    q_foodstuffs = ''
    Q_foodstuffs = ''
    M_foodstuffs = ''
    
    def get_hobbys_count(self):
        count_f = Food.objects.filter(foodstuffs__food=self).count()
        return count_f

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        
        # 絞り込み条件の設定
        foodstuffs = Foodstuff.objects.all()
        context['foodstuffs'] = foodstuffs
        
        categorys = Category.objects.all()
        context['categorys'] = categorys

        foods = Food.objects.all()
        context['foods'] = foods

        C = []
        for category in categorys:
            B = category.foodstuff_set.all()
            D = {"name": category.name, "foodstuff": B}
            C.append(D)

        context['stuff'] = C 
       
        # context['C_list'] = Food.objects.foodstuffs.all().annotate(
        #     match_count = Count('foodcategory')).order_by('match_count')
       
        M = []
        for food in foods :
            M = food.foodstuffs.all().annotate(
               match_count = Count('category'))
       
        context['M_count'] = M
        

        context['q_foodstuffs'] = self.q_foodstuffs
        context['Q_foodstuffs'] = self.Q_foodstuffs
        context['M_foodstuffs'] = self.M_foodstuffs

        return context
 
    def get_queryset(self):

        foods = self.model.objects.all()
        
        q_foodstuffs = self.request.GET.getlist('cb_foodstuff')    
        Q = len(q_foodstuffs)
        M = []
        # M = Food.foodstuffs.count()
        # N = Food.objects.filter(foodstuffs__in=q_foodstuffs).count()


        # C = self.model.objects.filter(foodstuffs__food=self).annotate()
       
       #確認用
        self.q_foodstuffs = q_foodstuffs
        self.Q_foodstuffs = Q
        self.M_foodstuffs = M

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

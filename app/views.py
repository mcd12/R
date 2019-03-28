
from django.views.generic import ListView
from django.db.models import Count
from .models import Food, Foodstuff,Category


class FoodListView(ListView):

    model =  Food
    context_object_name = "Food"
    queryset = Food.objects.prefetch_related('foodstuffs')

    q_foodstuffs = ''
    Q_foodstuffs = ''
    C_foodstuffs = ''
    M_foodstuffs = ''
    M_filter = ''
    foods_count = ''
    A_foodstuffs = ''
    foodid = ''

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        
        # 絞り込み条件の設定
        foodstuffs = Foodstuff.objects.all()
        context['foodstuffs'] = foodstuffs

        categorys = Category.objects.all()
        context['categorys'] = categorys

        foods = self.model.objects.all()
        context['foods'] = foods


# これができているディクショナリー
        SS = []
        for foodstuff in foodstuffs :
            fl = foodstuff.food_set.all().values('id')
            SS.append(fl)
        context['foodid'] = SS

# カテゴリー別のクエリを作成
        C1 = foodstuffs.filter(category_id=1)
        C1 = C1.annotate(co=Count('food')).order_by('-co')
        context['C1'] = C1

        C2 = foodstuffs.filter(category_id=2)
        C2 = C2.annotate(co=Count('food')).order_by('-co')
        context['C2'] = C2

        C3 = foodstuffs.filter(category_id=3)
        C3 = C3.annotate(co=Count('food')).order_by('-co')
        context['C3'] = C3

        C4 = foodstuffs.filter(category_id=4)
        C4 = C4.annotate(co=Count('food')).order_by('-co')
        context['C4'] = C4
       
        BB = []
        for category in categorys:
            B = category.foodstuff_set.all()
            Bid = category.foodstuff_set.all().values('id')
            BB.append(B)

        C = []
        for category in categorys:
            B = category.foodstuff_set.all()
            D = {"ename": category.ename, "foodstuff":B}
            C.append(D)
        context['stuff'] = C 
        

        T = []
        for AAA in foodstuffs:
            A = AAA.food_set.all()
            ID = A.values('id')
            T.append(ID)

        context['foodids'] = C 
        
        # フードが持っている素材のID
        
        for food in foods :
            hasid = food.foodstuffs.all()
        context['hasid'] = hasid
    
        
        C = []
        for food in foods:
            N = food.foodstuffs.count()
            C.append(N)
        self.C_foodstuffs = C

        context['q_foodstuffs'] = self.q_foodstuffs
        context['Q_foodstuffs'] = self.Q_foodstuffs
        context['C_foodstuffs'] = self.C_foodstuffs
        context['M_foodstuffs'] = self.M_foodstuffs
        context['M_filter'] = self.M_filter
        context['foods_count'] = self.foods_count
        context['A_foodstuffs'] = self.A_foodstuffs
        context['foods_ids'] = self.foods_ids
        context['foodstuff_id_set'] = self.foodstuff_id_set
       
        return context
 

    def get_queryset(self):

        foods = self.model.objects.all().order_by('foodcategory_id')
    
        q_foodstuffs = self.request.GET.getlist('cb_foodstuff')    
        Q = len(q_foodstuffs)

        #確認用
        self.q_foodstuffs = q_foodstuffs
        self.Q_foodstuffs = Q
           
        foods_count = foods.count()
        self.foods_count = foods_count


        M = Food.objects.values('id', 'name','foodstuffs')
       
        MM = []
        for m in M :
            MM.append(m)
        self.A_foodstuffs = MM
        
        # foodのIDを取得
        foods_ids = foods.values('id')
        self.foods_ids = foods_ids

        IDs = []
        for foods_id in foods_ids :
            ID = []
            for m in M :
                if foods_id['id'] == m['id']:
                    ID.append(str(m['foodstuffs']))
            MC_set = set(ID) & set(q_foodstuffs)
            MC = len(MC_set)
            IDs.append(MC)
        self.M_foodstuffs = IDs
        
        foodstuffs = Foodstuff.objects.all()
        D = []
        for foodstuff in foodstuffs:
            E = foodstuff.food_set.all()
            F = E.values('id')
            D.append(F)
        self.foodstuff_id_set = D
        
        C = []
        for food in foods:
            N = food.foodstuffs.count()
            C.append(N)
        self.C_foodstuffs = C
        
      
    # フィルター        
        # if len(q_foodstuffs) != 0:
        #     foods = foods.annotate(C_foodstuffs=Count('foodstuffs')).filter(C_foodstuffs__lte=MC)
       
        # if len(q_foodstuffs) != 0:
        #     foods = foods.filter(foodstuffs__in=q_foodstuffs).distinct().order_by('foodcategory_id')

        if len(q_foodstuffs) != 0:

            A = foods.filter(foodstuffs__in=q_foodstuffs).distinct()
            foods = A.annotate(co=Count('foodstuffs')).order_by('-co','foodcategory_id')
       
# よくわからないがマッチしている材料順にならんでいる・・・
# foods = A.annotate(co=Count('foodstuffs')).order_by('-co')
        return foods

    
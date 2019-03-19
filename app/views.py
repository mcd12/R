
from django.views.generic import ListView
from .models import Food, Foodstuff

#チェックボックスをつくる
class FoodListView(ListView):

    model =  Food

    # context_object_name = "foods"
    

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        
        # 絞り込み条件の設定
        foodstuffs = Foodstuff.objects.all()
        context['foodstuffs'] = foodstuffs
        
        return context
    
    def get_queryset(self):
    # デフォルトは全件取得
     results = self.model.objects.all()

    # GETのURLクエリパラメータを取得する
    # 該当のクエリパラメータが存在しない場合は、[]が返ってくる
     q_foodstuffs = self.request.GET.getlist('foodstuff')    

     if len(q_foodstuffs) != 0:
        results = results.filter(foodstuffs__in=q_foodstuffs).distinct()
        
     return results

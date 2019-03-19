from django import template
#クエリパラメータとフォーム状態とを連動
register = template.Library()

@register.filter
def checked(value, querydict):
    foodstuffs = querydict.getlist('foodstuff')
    if str(value) in foodstuffs:
        return "checked"
    return ""

@register.filter
def active(value):
    if value is None:
        return "active"
    return ""

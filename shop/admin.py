from django.contrib import admin

# Register your models here.
from shop.models import *


admin.site.register(ShopItem, admin.ModelAdmin)
admin.site.register(Order, admin.ModelAdmin)
admin.site.register(OrderItem, admin.ModelAdmin)
admin.site.register(Categories, admin.ModelAdmin)
admin.site.register(Feeds, admin.ModelAdmin)
admin.site.register(FeedbackModel, admin.ModelAdmin)

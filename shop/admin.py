from django.contrib import admin
import django.utils.safestring
# Register your models here.
from shop.models import *


@admin.register(ShopItem)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'price', 'image', 'post_date']


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'phone', 'comments']
    list_editable = ['comments']


@admin.register(Feeds)
class FeedsAdmin(admin.ModelAdmin):
    list_display = ['title', 'news_category', 'news_post_date']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category', 'category_image']

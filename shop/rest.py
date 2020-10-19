from rest_framework import permissions

from shop.models import *
from rest_framework.serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAdminUser

__all__ = 'ProductSerializer', 'ProductViewSet'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ShopItem
        fields = '__all__'


class ProductViewSet(ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = '__all__'


class FeedbackViewSet(ModelViewSet):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUser]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class FeedsSerializer(ModelSerializer):
    class Meta:
        model = Feeds
        fields = '__all__'


class FeedsViewSet(ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer
    permission_classes = [IsAdminUser]


router = DefaultRouter()
router.register('product', ProductViewSet, 'product')
router.register('category', CategoryViewSet, 'category')
router.register('feeds', FeedsViewSet, 'feeds')
router.register('feedback', FeedbackViewSet, 'feedback')
